#!/usr/bin/env python3
"""
Email Reader Script
A comprehensive script to read emails from various email providers via IMAP.
Supports Gmail, Outlook, Yahoo, and other IMAP-compatible email services.
"""

import imaplib
import email
import os
import json
import getpass
from email.header import decode_header
from datetime import datetime
from typing import List, Dict, Optional
import argparse


class EmailReader:
    """A class to read emails from various email providers."""
    
    def __init__(self, email_address: str, password: str = None, provider: str = "auto"):
        """
        Initialize the email reader.
        
        Args:
            email_address: The email address to connect to
            password: The password or app password (if None, will prompt)
            provider: Email provider ("gmail", "outlook", "yahoo", "auto")
        """
        self.email_address = email_address
        self.password = password or getpass.getpass(f"Enter password for {email_address}: ")
        self.provider = self._detect_provider(provider, email_address)
        self.imap_server = self._get_imap_server()
        self.connection = None
        
    def _detect_provider(self, provider: str, email_address: str) -> str:
        """Detect email provider based on email address."""
        if provider != "auto":
            return provider
            
        domain = email_address.split('@')[1].lower()
        if 'gmail' in domain:
            return 'gmail'
        elif 'outlook' in domain or 'hotmail' in domain or 'live' in domain:
            return 'outlook'
        elif 'yahoo' in domain:
            return 'yahoo'
        else:
            return 'generic'
    
    def _get_imap_server(self) -> Dict[str, str]:
        """Get IMAP server settings for the provider."""
        servers = {
            'gmail': {
                'server': 'imap.gmail.com',
                'port': 993,
                'use_ssl': True
            },
            'outlook': {
                'server': 'outlook.office365.com',
                'port': 993,
                'use_ssl': True
            },
            'yahoo': {
                'server': 'imap.mail.yahoo.com',
                'port': 993,
                'use_ssl': True
            },
            'generic': {
                'server': 'imap.example.com',  # You'll need to update this
                'port': 993,
                'use_ssl': True
            }
        }
        return servers.get(self.provider, servers['generic'])
    
    def connect(self) -> bool:
        """Connect to the email server."""
        try:
            if self.imap_server['use_ssl']:
                self.connection = imaplib.IMAP4_SSL(
                    self.imap_server['server'], 
                    self.imap_server['port']
                )
            else:
                self.connection = imaplib.IMAP4(
                    self.imap_server['server'], 
                    self.imap_server['port']
                )
            
            # Login
            self.connection.login(self.email_address, self.password)
            print(f"Successfully connected to {self.provider}")
            return True
            
        except Exception as e:
            print(f"Failed to connect: {e}")
            return False
    
    def disconnect(self):
        """Disconnect from the email server."""
        if self.connection:
            self.connection.logout()
            print("Disconnected from email server")
    
    def list_folders(self) -> List[str]:
        """List all available email folders."""
        if not self.connection:
            print("Not connected. Call connect() first.")
            return []
        
        try:
            _, folders = self.connection.list()
            folder_names = []
            for folder in folders:
                folder_name = folder.decode().split('"')[-2]
                folder_names.append(folder_name)
            return folder_names
        except Exception as e:
            print(f"Error listing folders: {e}")
            return []
    
    def select_folder(self, folder_name: str = "INBOX") -> bool:
        """Select an email folder."""
        if not self.connection:
            print("Not connected. Call connect() first.")
            return False
        
        try:
            status, messages = self.connection.select(folder_name)
            if status == 'OK':
                print(f"Selected folder: {folder_name}")
                return True
            else:
                print(f"Failed to select folder: {folder_name}")
                return False
        except Exception as e:
            print(f"Error selecting folder: {e}")
            return False
    
    def get_email_count(self) -> int:
        """Get the total number of emails in the selected folder."""
        if not self.connection:
            return 0
        
        try:
            _, messages = self.connection.search(None, 'ALL')
            return len(messages[0].split())
        except Exception as e:
            print(f"Error getting email count: {e}")
            return 0
    
    def read_email(self, email_id: str) -> Dict:
        """Read a specific email by ID."""
        if not self.connection:
            return {}
        
        try:
            _, msg_data = self.connection.fetch(email_id, '(RFC822)')
            email_body = msg_data[0][1]
            email_message = email.message_from_bytes(email_body)
            
            return self._parse_email(email_message)
            
        except Exception as e:
            print(f"Error reading email {email_id}: {e}")
            return {}
    
    def _parse_email(self, email_message) -> Dict:
        """Parse email message into a structured format."""
        email_data = {
            'subject': '',
            'from': '',
            'to': '',
            'date': '',
            'body': '',
            'attachments': []
        }
        
        # Parse headers
        for header in ['subject', 'from', 'to', 'date']:
            value = email_message.get(header, '')
            if value:
                decoded_value = decode_header(value)[0][0]
                if isinstance(decoded_value, bytes):
                    decoded_value = decoded_value.decode()
                email_data[header] = decoded_value
        
        # Parse body
        email_data['body'] = self._get_email_body(email_message)
        
        # Parse attachments
        email_data['attachments'] = self._get_attachments(email_message)
        
        return email_data
    
    def _get_email_body(self, email_message) -> str:
        """Extract email body text."""
        body = ""
        
        if email_message.is_multipart():
            for part in email_message.walk():
                content_type = part.get_content_type()
                content_disposition = str(part.get("Content-Disposition"))
                
                if content_type == "text/plain" and "attachment" not in content_disposition:
                    try:
                        body = part.get_payload(decode=True).decode()
                        break
                    except:
                        pass
        else:
            try:
                body = email_message.get_payload(decode=True).decode()
            except:
                body = str(email_message.get_payload())
        
        return body
    
    def _get_attachments(self, email_message) -> List[Dict]:
        """Extract email attachments."""
        attachments = []
        
        if email_message.is_multipart():
            for part in email_message.walk():
                content_disposition = str(part.get("Content-Disposition"))
                
                if "attachment" in content_disposition:
                    filename = part.get_filename()
                    if filename:
                        attachments.append({
                            'filename': filename,
                            'content_type': part.get_content_type(),
                            'size': len(part.get_payload())
                        })
        
        return attachments
    
    def search_emails(self, criteria: str, limit: int = 10) -> List[Dict]:
        """Search emails using IMAP search criteria."""
        if not self.connection:
            return []
        
        try:
            _, message_ids = self.connection.search(None, criteria)
            email_ids = message_ids[0].split()
            
            # Limit results
            if limit:
                email_ids = email_ids[-limit:]  # Get most recent emails
            
            emails = []
            for email_id in email_ids:
                email_data = self.read_email(email_id)
                if email_data:
                    email_data['id'] = email_id.decode()
                    emails.append(email_data)
            
            return emails
            
        except Exception as e:
            print(f"Error searching emails: {e}")
            return []
    
    def get_recent_emails(self, limit: int = 10) -> List[Dict]:
        """Get the most recent emails."""
        return self.search_emails('ALL', limit)
    
    def get_unread_emails(self, limit: int = 10) -> List[Dict]:
        """Get unread emails."""
        return self.search_emails('UNSEEN', limit)
    
    def mark_as_read(self, email_id: str) -> bool:
        """Mark an email as read."""
        if not self.connection:
            return False
        
        try:
            self.connection.store(email_id, '+FLAGS', '\\Seen')
            return True
        except Exception as e:
            print(f"Error marking email as read: {e}")
            return False
    
    def delete_email(self, email_id: str) -> bool:
        """Delete an email."""
        if not self.connection:
            return False
        
        try:
            self.connection.store(email_id, '+FLAGS', '\\Deleted')
            self.connection.expunge()
            return True
        except Exception as e:
            print(f"Error deleting email: {e}")
            return False


def save_emails_to_json(emails: List[Dict], filename: str):
    """Save emails to a JSON file."""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(emails, f, indent=2, ensure_ascii=False, default=str)
        print(f"Emails saved to {filename}")
    except Exception as e:
        print(f"Error saving emails: {e}")


def print_email_summary(email_data: Dict):
    """Print a formatted email summary."""
    print(f"\n{'='*60}")
    print(f"Subject: {email_data.get('subject', 'No subject')}")
    print(f"From: {email_data.get('from', 'Unknown')}")
    print(f"Date: {email_data.get('date', 'Unknown')}")
    print(f"Body: {email_data.get('body', 'No body')[:100]}...")
    if email_data.get('attachments'):
        print(f"Attachments: {len(email_data['attachments'])} files")
    print(f"{'='*60}")


def main():
    """Main function to demonstrate email reading."""
    parser = argparse.ArgumentParser(description='Read emails from various providers')
    parser.add_argument('--email', required=True, help='Email address')
    parser.add_argument('--password', help='Password (will prompt if not provided)')
    parser.add_argument('--provider', default='auto', 
                       choices=['gmail', 'outlook', 'yahoo', 'auto'],
                       help='Email provider')
    parser.add_argument('--folder', default='INBOX', help='Email folder to read')
    parser.add_argument('--limit', type=int, default=5, help='Number of emails to read')
    parser.add_argument('--search', help='Search criteria (e.g., "FROM someone@example.com")')
    parser.add_argument('--unread', action='store_true', help='Only read unread emails')
    parser.add_argument('--save', help='Save emails to JSON file')
    
    args = parser.parse_args()
    
    # Create email reader
    reader = EmailReader(args.email, args.password, args.provider)
    
    # Connect to server
    if not reader.connect():
        return
    
    try:
        # Select folder
        if not reader.select_folder(args.folder):
            return
        
        # Get emails based on criteria
        if args.search:
            emails = reader.search_emails(args.search, args.limit)
        elif args.unread:
            emails = reader.get_unread_emails(args.limit)
        else:
            emails = reader.get_recent_emails(args.limit)
        
        # Display emails
        print(f"\nFound {len(emails)} emails:")
        for email_data in emails:
            print_email_summary(email_data)
        
        # Save to file if requested
        if args.save and emails:
            save_emails_to_json(emails, args.save)
    
    finally:
        reader.disconnect()


if __name__ == "__main__":
    # Example usage without command line arguments
    print("Email Reader Script")
    print("=" * 50)
    
    # You can also use the script interactively
    email_address = input("Enter your email address: ")
    
    reader = EmailReader(email_address)
    
    if reader.connect():
        try:
            # List available folders
            print("\nAvailable folders:")
            folders = reader.list_folders()
            for folder in folders:
                print(f"  - {folder}")
            
            # Select INBOX and get recent emails
            if reader.select_folder("INBOX"):
                emails = reader.get_recent_emails(3)
                print(f"\nRecent emails ({len(emails)}):")
                for email_data in emails:
                    print_email_summary(email_data)
        
        finally:
            reader.disconnect() 