#!/usr/bin/env python3
"""
macOS Mail Client Access Script
Directly interacts with the active Mail app on macOS using AppleScript.
This script can read emails, get account information, and perform actions
on the currently active Mail client.
"""

import subprocess
import json
import re
from typing import List, Dict, Optional, Any
from datetime import datetime
import os


class MacMailClient:
    """A class to interact with the macOS Mail app using AppleScript."""
    
    def __init__(self):
        """Initialize the Mail client access."""
        self.mail_app = "Mail"
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        
    def _run_applescript(self, script: str) -> str:
        """Run an AppleScript and return the result."""
        try:
            result = subprocess.run(
                ['osascript', '-e', script],
                capture_output=True,
                text=True,
                timeout=30
            )
            if result.returncode == 0:
                return result.stdout.strip()
            else:
                print(f"AppleScript error: {result.stderr}")
                return ""
        except subprocess.TimeoutExpired:
            print("AppleScript execution timed out")
            return ""
        except Exception as e:
            print(f"Error running AppleScript: {e}")
            return ""
    
    def is_mail_running(self) -> bool:
        """Check if Mail app is running."""
        script = f'''
        tell application "System Events"
            return (name of processes) contains "{self.mail_app}"
        end tell
        '''
        result = self._run_applescript(script)
        return result.lower() == "true"
    
    def activate_mail(self) -> bool:
        """Activate the Mail app (bring to front)."""
        script = f'''
        tell application "{self.mail_app}"
            activate
        end tell
        '''
        result = self._run_applescript(script)
        return result == ""
    
    def get_mail_accounts(self) -> List[Dict[str, str]]:
        """Get all email accounts configured in Mail."""
        script = '''
        tell application "Mail"
            set accountList to {}
            repeat with theAccount in accounts
                set accountInfo to {{name:name of theAccount, email:user name of theAccount, type:class of theAccount as string}}
                copy accountInfo to end of accountList
            end repeat
            return accountList
        end tell
        '''
        result = self._run_applescript(script)
        return self._parse_account_list(result)
    
    def _parse_account_list(self, result: str) -> List[Dict[str, str]]:
        """Parse the account list from AppleScript result."""
        accounts = []
        if result:
            # Parse the AppleScript result format
            lines = result.split('\n')
            current_account = {}
            for line in lines:
                line = line.strip()
                if line.startswith('name:'):
                    if current_account:
                        accounts.append(current_account)
                    current_account = {'name': line.split(':', 1)[1].strip()}
                elif line.startswith('email:'):
                    current_account['email'] = line.split(':', 1)[1].strip()
                elif line.startswith('type:'):
                    current_account['type'] = line.split(':', 1)[1].strip()
            if current_account:
                accounts.append(current_account)
        return accounts
    
    def get_mailboxes(self) -> List[Dict[str, str]]:
        """Get all mailboxes/folders in Mail."""
        script = '''
        tell application "Mail"
            set mailboxList to {}
            repeat with theMailbox in mailboxes
                set mailboxInfo to {{name:name of theMailbox, account:name of account of theMailbox, unread:unread count of theMailbox, total:count of messages of theMailbox}}
                copy mailboxInfo to end of mailboxList
            end repeat
            return mailboxList
        end tell
        '''
        result = self._run_applescript(script)
        return self._parse_mailbox_list(result)
    
    def _parse_mailbox_list(self, result: str) -> List[Dict[str, str]]:
        """Parse the mailbox list from AppleScript result."""
        mailboxes = []
        if result:
            # Parse the AppleScript result format
            lines = result.split('\n')
            current_mailbox = {}
            for line in lines:
                line = line.strip()
                if line.startswith('name:'):
                    if current_mailbox:
                        mailboxes.append(current_mailbox)
                    current_mailbox = {'name': line.split(':', 1)[1].strip()}
                elif line.startswith('account:'):
                    current_mailbox['account'] = line.split(':', 1)[1].strip()
                elif line.startswith('unread:'):
                    current_mailbox['unread'] = line.split(':', 1)[1].strip()
                elif line.startswith('total:'):
                    current_mailbox['total'] = line.split(':', 1)[1].strip()
            if current_mailbox:
                mailboxes.append(current_mailbox)
        return mailboxes
    
    def get_selected_messages(self) -> List[Dict[str, Any]]:
        """Get currently selected messages in Mail."""
        script = '''
        tell application "Mail"
            set selectedMessages to {}
            set theSelection to selection
            repeat with theMessage in theSelection
                set messageInfo to {{subject:subject of theMessage, sender:sender of theMessage, date:date received of theMessage, read:read status of theMessage, id:id of theMessage}}
                copy messageInfo to end of selectedMessages
            end repeat
            return selectedMessages
        end tell
        '''
        result = self._run_applescript(script)
        return self._parse_message_list(result)
    
    def get_messages_from_mailbox(self, mailbox_name: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Get messages from a specific mailbox."""
        script = f'''
        tell application "Mail"
            set messageList to {{}}
            set theMailbox to mailbox "{mailbox_name}"
            set theMessages to messages of theMailbox
            set messageCount to count of theMessages
            set startIndex to (messageCount - {limit} + 1)
            if startIndex < 1 then set startIndex to 1
            
            repeat with i from startIndex to messageCount
                set theMessage to item i of theMessages
                set messageInfo to {{subject:subject of theMessage, sender:sender of theMessage, date:date received of theMessage, read:read status of theMessage, id:id of theMessage}}
                copy messageInfo to end of messageList
            end repeat
            return messageList
        end tell
        '''
        result = self._run_applescript(script)
        return self._parse_message_list(result)
    
    def _parse_message_list(self, result: str) -> List[Dict[str, Any]]:
        """Parse the message list from AppleScript result."""
        messages = []
        if result:
            # Parse the AppleScript result format
            lines = result.split('\n')
            current_message = {}
            for line in lines:
                line = line.strip()
                if line.startswith('subject:'):
                    if current_message:
                        messages.append(current_message)
                    current_message = {'subject': line.split(':', 1)[1].strip()}
                elif line.startswith('sender:'):
                    current_message['sender'] = line.split(':', 1)[1].strip()
                elif line.startswith('date:'):
                    current_message['date'] = line.split(':', 1)[1].strip()
                elif line.startswith('read:'):
                    current_message['read'] = line.split(':', 1)[1].strip().lower() == 'true'
                elif line.startswith('id:'):
                    current_message['id'] = line.split(':', 1)[1].strip()
            if current_message:
                messages.append(current_message)
        return messages
    
    def get_message_content(self, message_id: str) -> Dict[str, Any]:
        """Get the full content of a specific message."""
        script = f'''
        tell application "Mail"
            set theMessage to message id "{message_id}"
            set messageContent to {{subject:subject of theMessage, sender:sender of theMessage, date:date received of theMessage, content:content of theMessage, read:read status of theMessage, id:id of theMessage}}
            return messageContent
        end tell
        '''
        result = self._run_applescript(script)
        return self._parse_message_content(result)
    
    def _parse_message_content(self, result: str) -> Dict[str, Any]:
        """Parse the message content from AppleScript result."""
        message = {}
        if result:
            lines = result.split('\n')
            for line in lines:
                line = line.strip()
                if line.startswith('subject:'):
                    message['subject'] = line.split(':', 1)[1].strip()
                elif line.startswith('sender:'):
                    message['sender'] = line.split(':', 1)[1].strip()
                elif line.startswith('date:'):
                    message['date'] = line.split(':', 1)[1].strip()
                elif line.startswith('content:'):
                    message['content'] = line.split(':', 1)[1].strip()
                elif line.startswith('read:'):
                    message['read'] = line.split(':', 1)[1].strip().lower() == 'true'
                elif line.startswith('id:'):
                    message['id'] = line.split(':', 1)[1].strip()
        return message
    
    def mark_message_as_read(self, message_id: str) -> bool:
        """Mark a message as read."""
        script = f'''
        tell application "Mail"
            set theMessage to message id "{message_id}"
            set read status of theMessage to true
        end tell
        '''
        result = self._run_applescript(script)
        return result == ""
    
    def mark_message_as_unread(self, message_id: str) -> bool:
        """Mark a message as unread."""
        script = f'''
        tell application "Mail"
            set theMessage to message id "{message_id}"
            set read status of theMessage to false
        end tell
        '''
        result = self._run_applescript(script)
        return result == ""
    
    def delete_message(self, message_id: str) -> bool:
        """Delete a message."""
        script = f'''
        tell application "Mail"
            set theMessage to message id "{message_id}"
            delete theMessage
        end tell
        '''
        result = self._run_applescript(script)
        return result == ""
    
    def search_messages(self, search_term: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Search for messages using Mail's search functionality."""
        script = f'''
        tell application "Mail"
            set searchResults to {{}}
            set theMessages to messages of inbox whose subject contains "{search_term}" or content contains "{search_term}"
            set messageCount to count of theMessages
            set startIndex to (messageCount - {limit} + 1)
            if startIndex < 1 then set startIndex to 1
            
            repeat with i from startIndex to messageCount
                set theMessage to item i of theMessages
                set messageInfo to {{subject:subject of theMessage, sender:sender of theMessage, date:date received of theMessage, read:read status of theMessage, id:id of theMessage}}
                copy messageInfo to end of searchResults
            end repeat
            return searchResults
        end tell
        '''
        result = self._run_applescript(script)
        return self._parse_message_list(result)
    
    def get_unread_count(self) -> int:
        """Get the total number of unread messages."""
        script = '''
        tell application "Mail"
            set unreadCount to 0
            repeat with theMailbox in mailboxes
                set unreadCount to unreadCount + (unread count of theMailbox)
            end repeat
            return unreadCount
        end tell
        '''
        result = self._run_applescript(script)
        try:
            return int(result) if result else 0
        except ValueError:
            return 0
    
    def refresh_mail(self) -> bool:
        """Refresh all mail accounts."""
        script = '''
        tell application "Mail"
            check for new mail
        end tell
        '''
        result = self._run_applescript(script)
        return result == ""
    
    def create_new_message(self, to: str = "", subject: str = "", content: str = "") -> bool:
        """Create a new message (opens compose window)."""
        script = f'''
        tell application "Mail"
            set newMessage to make new outgoing message with properties {{subject:"{subject}", content:"{content}"}}
            if "{to}" is not "" then
                set recipient of newMessage to "{to}"
            end if
            activate
        end tell
        '''
        result = self._run_applescript(script)
        return result == ""
    
    def reply_to_message(self, message_id: str) -> bool:
        """Reply to a specific message."""
        script = f'''
        tell application "Mail"
            set theMessage to message id "{message_id}"
            set replyMessage to reply theMessage
            activate
        end tell
        '''
        result = self._run_applescript(script)
        return result == ""
    
    def forward_message(self, message_id: str) -> bool:
        """Forward a specific message."""
        script = f'''
        tell application "Mail"
            set theMessage to message id "{message_id}"
            set forwardMessage to forward theMessage
            activate
        end tell
        '''
        result = self._run_applescript(script)
        return result == ""


def save_to_json(data: Any, filename: str):
    """Save data to a JSON file."""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False, default=str)
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"Error saving data: {e}")


def print_mail_info(mail_client: MacMailClient):
    """Print comprehensive Mail app information."""
    print("📧 macOS Mail Client Information")
    print("=" * 50)
    
    # Check if Mail is running
    if mail_client.is_mail_running():
        print("✅ Mail app is running")
        mail_client.activate_mail()
    else:
        print("❌ Mail app is not running")
        return
    
    # Get accounts
    print("\n📋 Email Accounts:")
    accounts = mail_client.get_mail_accounts()
    for account in accounts:
        print(f"  - {account.get('name', 'Unknown')} ({account.get('email', 'No email')}) - {account.get('type', 'Unknown type')}")
    
    # Get unread count
    unread_count = mail_client.get_unread_count()
    print(f"\n📬 Total unread messages: {unread_count}")
    
    # Get mailboxes
    print("\n📁 Mailboxes:")
    mailboxes = mail_client.get_mailboxes()
    for mailbox in mailboxes:
        print(f"  - {mailbox.get('name', 'Unknown')} ({mailbox.get('unread', '0')} unread, {mailbox.get('total', '0')} total)")
    
    # Get recent messages from inbox
    print("\n📨 Recent Messages from Inbox:")
    messages = mail_client.get_messages_from_mailbox("INBOX", 5)
    for i, message in enumerate(messages, 1):
        print(f"  {i}. {message.get('subject', 'No subject')}")
        print(f"     From: {message.get('sender', 'Unknown')}")
        print(f"     Date: {message.get('date', 'Unknown')}")
        print(f"     Read: {'Yes' if message.get('read', True) else 'No'}")
        print()


def main():
    """Main function to demonstrate Mail client access."""
    mail_client = MacMailClient()
    
    print("macOS Mail Client Access")
    print("=" * 50)
    
    # Check if Mail is running
    if not mail_client.is_mail_running():
        print("❌ Mail app is not running. Please open Mail first.")
        return
    
    # Activate Mail
    mail_client.activate_mail()
    print("✅ Mail app activated")
    
    # Print comprehensive information
    print_mail_info(mail_client)
    
    # Interactive menu
    while True:
        print("\n🔧 Available Actions:")
        print("1. Get selected messages")
        print("2. Search messages")
        print("3. Get unread count")
        print("4. Refresh mail")
        print("5. Create new message")
        print("6. Save current data to JSON")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == "1":
            messages = mail_client.get_selected_messages()
            if messages:
                print(f"\n📨 Selected Messages ({len(messages)}):")
                for i, message in enumerate(messages, 1):
                    print(f"  {i}. {message.get('subject', 'No subject')}")
                    print(f"     From: {message.get('sender', 'Unknown')}")
            else:
                print("No messages selected in Mail")
        
        elif choice == "2":
            search_term = input("Enter search term: ").strip()
            if search_term:
                results = mail_client.search_messages(search_term, 5)
                print(f"\n🔍 Search Results ({len(results)}):")
                for i, message in enumerate(results, 1):
                    print(f"  {i}. {message.get('subject', 'No subject')}")
                    print(f"     From: {message.get('sender', 'Unknown')}")
        
        elif choice == "3":
            unread_count = mail_client.get_unread_count()
            print(f"\n📬 Unread messages: {unread_count}")
        
        elif choice == "4":
            if mail_client.refresh_mail():
                print("✅ Mail refreshed")
            else:
                print("❌ Failed to refresh mail")
        
        elif choice == "5":
            to_email = input("To (optional): ").strip()
            subject = input("Subject (optional): ").strip()
            content = input("Content (optional): ").strip()
            if mail_client.create_new_message(to_email, subject, content):
                print("✅ New message window opened")
            else:
                print("❌ Failed to create new message")
        
        elif choice == "6":
            filename = input("Enter filename (default: mail_data.json): ").strip()
            if not filename:
                filename = "mail_data.json"
            
            data = {
                'accounts': mail_client.get_mail_accounts(),
                'mailboxes': mail_client.get_mailboxes(),
                'unread_count': mail_client.get_unread_count(),
                'recent_messages': mail_client.get_messages_from_mailbox("INBOX", 10),
                'timestamp': datetime.now().isoformat()
            }
            save_to_json(data, filename)
        
        elif choice == "7":
            print("👋 Goodbye!")
            break
        
        else:
            print("❌ Invalid choice. Please enter 1-7.")


if __name__ == "__main__":
    main() 