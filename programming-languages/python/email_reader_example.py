#!/usr/bin/env python3
"""
Simple example of how to use the EmailReader class.
This script demonstrates basic email reading functionality.
"""

from email_reader import EmailReader, print_email_summary, save_emails_to_json


def main():
    """Example usage of the EmailReader."""
    
    print("Email Reader Example")
    print("=" * 50)
    
    # Get email credentials
    email_address = input("Enter your email address: ")
    
    # Create email reader instance
    reader = EmailReader(email_address)
    
    # Connect to email server
    if not reader.connect():
        print("Failed to connect to email server.")
        return
    
    try:
        # List available folders
        print("\nAvailable email folders:")
        folders = reader.list_folders()
        for folder in folders:
            print(f"  - {folder}")
        
        # Select INBOX
        if not reader.select_folder("INBOX"):
            print("Failed to select INBOX folder.")
            return
        
        # Get email count
        email_count = reader.get_email_count()
        print(f"\nTotal emails in INBOX: {email_count}")
        
        # Get recent emails
        print("\nFetching recent emails...")
        recent_emails = reader.get_recent_emails(5)
        
        if recent_emails:
            print(f"\nFound {len(recent_emails)} recent emails:")
            for i, email_data in enumerate(recent_emails, 1):
                print(f"\n--- Email {i} ---")
                print_email_summary(email_data)
            
            # Save emails to JSON file
            save_choice = input("\nSave emails to JSON file? (y/n): ").lower()
            if save_choice == 'y':
                filename = input("Enter filename (default: emails.json): ").strip()
                if not filename:
                    filename = "emails.json"
                save_emails_to_json(recent_emails, filename)
        
        # Get unread emails
        print("\nFetching unread emails...")
        unread_emails = reader.get_unread_emails(10)
        
        if unread_emails:
            print(f"\nFound {len(unread_emails)} unread emails:")
            for i, email_data in enumerate(unread_emails, 1):
                print(f"\n--- Unread Email {i} ---")
                print_email_summary(email_data)
        else:
            print("No unread emails found.")
        
        # Search for specific emails
        print("\nSearch functionality:")
        search_choice = input("Search for emails? (y/n): ").lower()
        if search_choice == 'y':
            search_criteria = input("Enter search criteria (e.g., 'FROM someone@example.com'): ").strip()
            if search_criteria:
                search_results = reader.search_emails(search_criteria, 5)
                if search_results:
                    print(f"\nFound {len(search_results)} emails matching criteria:")
                    for i, email_data in enumerate(search_results, 1):
                        print(f"\n--- Search Result {i} ---")
                        print_email_summary(email_data)
                else:
                    print("No emails found matching the criteria.")
    
    finally:
        # Always disconnect
        reader.disconnect()
        print("\nDisconnected from email server.")


if __name__ == "__main__":
    main() 