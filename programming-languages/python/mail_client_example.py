#!/usr/bin/env python3
"""
Simple example of how to access the active macOS Mail client.
This script demonstrates basic Mail app interaction functionality.
"""

from mail_client_access import MacMailClient, save_to_json


def main():
    """Example usage of the MacMailClient."""
    
    print("📧 macOS Mail Client Access Example")
    print("=" * 50)
    
    # Create Mail client instance
    mail_client = MacMailClient()
    
    # Check if Mail is running
    if not mail_client.is_mail_running():
        print("❌ Mail app is not running. Please open Mail first.")
        print("💡 Tip: Open the Mail app and try again.")
        return
    
    print("✅ Mail app is running")
    
    # Activate Mail (bring to front)
    mail_client.activate_mail()
    print("✅ Mail app activated")
    
    # Get email accounts
    print("\n📋 Email Accounts:")
    accounts = mail_client.get_mail_accounts()
    if accounts:
        for account in accounts:
            print(f"  - {account.get('name', 'Unknown')} ({account.get('email', 'No email')})")
    else:
        print("  No accounts found")
    
    # Get unread count
    unread_count = mail_client.get_unread_count()
    print(f"\n📬 Total unread messages: {unread_count}")
    
    # Get recent messages from inbox
    print("\n📨 Recent Messages from Inbox:")
    messages = mail_client.get_messages_from_mailbox("INBOX", 3)
    if messages:
        for i, message in enumerate(messages, 1):
            print(f"  {i}. {message.get('subject', 'No subject')}")
            print(f"     From: {message.get('sender', 'Unknown')}")
            print(f"     Date: {message.get('date', 'Unknown')}")
            print(f"     Read: {'Yes' if message.get('read', True) else 'No'}")
            print()
    else:
        print("  No messages found in inbox")
    
    # Get selected messages (if any)
    print("📎 Selected Messages:")
    selected = mail_client.get_selected_messages()
    if selected:
        for i, message in enumerate(selected, 1):
            print(f"  {i}. {message.get('subject', 'No subject')}")
    else:
        print("  No messages selected")
    
    # Save data to JSON
    print("\n💾 Saving Mail data to JSON...")
    data = {
        'accounts': accounts,
        'unread_count': unread_count,
        'recent_messages': messages,
        'selected_messages': selected
    }
    save_to_json(data, "mail_data.json")
    
    print("\n✅ Mail client access completed!")


if __name__ == "__main__":
    main() 