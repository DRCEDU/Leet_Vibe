# macOS Mail Client Access Script

A Python script that directly accesses and interacts with the active macOS Mail app using AppleScript integration. This script can read emails, get account information, and perform various actions on your currently active Mail client.

## 🎯 Key Features

- ✅ **Direct Mail app access** - No need for IMAP credentials
- ✅ **Read emails** from any mailbox/folder
- ✅ **Get account information** and mailbox details
- ✅ **Search messages** using Mail's built-in search
- ✅ **Manage messages** - mark as read/unread, delete
- ✅ **Compose emails** - create new messages, reply, forward
- ✅ **Get selected messages** - access currently selected emails
- ✅ **Save data to JSON** for further processing
- ✅ **Real-time interaction** with the active Mail app

## 📋 Prerequisites

- **macOS** (this script only works on Mac)
- **Mail app** must be installed and running
- **Python 3.6+** (uses only built-in libraries)
- **Mail app permissions** - may need to grant accessibility permissions

## 🔧 Setup

### 1. Grant Accessibility Permissions (if needed)

If you encounter permission issues, you may need to grant accessibility permissions:

1. Go to **System Preferences** → **Security & Privacy** → **Privacy**
2. Select **Accessibility** from the left sidebar
3. Click the **lock icon** to make changes
4. Add **Terminal** or your Python IDE to the list
5. Check the box next to it

### 2. Install the Script

```bash
# Navigate to the script directory
cd programming-languages/python/

# Make scripts executable (optional)
chmod +x mail_client_access.py
chmod +x mail_client_example.py
```

## 🚀 Usage

### Quick Start

```bash
# Run the example script
python mail_client_example.py
```

### Interactive Mode

```bash
# Run the main script for interactive menu
python mail_client_access.py
```

### Programmatic Usage

```python
from mail_client_access import MacMailClient

# Create Mail client instance
mail_client = MacMailClient()

# Check if Mail is running
if mail_client.is_mail_running():
    # Activate Mail
    mail_client.activate_mail()
    
    # Get accounts
    accounts = mail_client.get_mail_accounts()
    
    # Get recent messages
    messages = mail_client.get_messages_from_mailbox("INBOX", 10)
    
    # Get unread count
    unread_count = mail_client.get_unread_count()
    
    print(f"Found {len(accounts)} accounts, {unread_count} unread messages")
```

## 📚 API Reference

### MacMailClient Class

#### Basic Operations

| Method | Description | Returns |
|--------|-------------|---------|
| `is_mail_running()` | Check if Mail app is running | `bool` |
| `activate_mail()` | Bring Mail app to front | `bool` |
| `get_mail_accounts()` | Get all email accounts | `List[Dict]` |
| `get_mailboxes()` | Get all mailboxes/folders | `List[Dict]` |
| `get_unread_count()` | Get total unread messages | `int` |

#### Message Operations

| Method | Description | Returns |
|--------|-------------|---------|
| `get_selected_messages()` | Get currently selected messages | `List[Dict]` |
| `get_messages_from_mailbox(mailbox, limit)` | Get messages from specific mailbox | `List[Dict]` |
| `get_message_content(message_id)` | Get full message content | `Dict` |
| `search_messages(term, limit)` | Search for messages | `List[Dict]` |

#### Message Management

| Method | Description | Returns |
|--------|-------------|---------|
| `mark_message_as_read(message_id)` | Mark message as read | `bool` |
| `mark_message_as_unread(message_id)` | Mark message as unread | `bool` |
| `delete_message(message_id)` | Delete a message | `bool` |

#### Composition

| Method | Description | Returns |
|--------|-------------|---------|
| `create_new_message(to, subject, content)` | Create new message | `bool` |
| `reply_to_message(message_id)` | Reply to message | `bool` |
| `forward_message(message_id)` | Forward message | `bool` |

#### Utilities

| Method | Description | Returns |
|--------|-------------|---------|
| `refresh_mail()` | Check for new mail | `bool` |

## 📊 Data Structures

### Account Information
```python
{
    'name': 'Account Name',
    'email': 'user@example.com',
    'type': 'Account Type'
}
```

### Message Information
```python
{
    'subject': 'Email Subject',
    'sender': 'sender@example.com',
    'date': 'Date String',
    'read': True/False,
    'id': 'Message ID',
    'content': 'Full message content'  # Only in get_message_content()
}
```

### Mailbox Information
```python
{
    'name': 'Mailbox Name',
    'account': 'Account Name',
    'unread': 'Unread Count',
    'total': 'Total Messages'
}
```

## 🔍 Examples

### Get Recent Emails
```python
mail_client = MacMailClient()
if mail_client.is_mail_running():
    messages = mail_client.get_messages_from_mailbox("INBOX", 5)
    for message in messages:
        print(f"Subject: {message['subject']}")
        print(f"From: {message['sender']}")
        print(f"Read: {message['read']}")
```

### Search for Messages
```python
# Search for messages containing "important"
results = mail_client.search_messages("important", 10)
for message in results:
    print(f"Found: {message['subject']}")
```

### Get Selected Messages
```python
# Get messages currently selected in Mail
selected = mail_client.get_selected_messages()
if selected:
    print(f"You have {len(selected)} messages selected")
    for message in selected:
        print(f"- {message['subject']}")
```

### Create New Message
```python
# Open compose window
mail_client.create_new_message(
    to="recipient@example.com",
    subject="Hello",
    content="This is a test message"
)
```

### Mark Messages as Read
```python
# Get unread messages and mark them as read
messages = mail_client.get_messages_from_mailbox("INBOX", 10)
for message in messages:
    if not message['read']:
        mail_client.mark_message_as_read(message['id'])
```

## 🛠️ Troubleshooting

### Common Issues

1. **"Mail app is not running"**
   - Open the Mail app first
   - Make sure it's not just in the dock but actually running

2. **Permission denied errors**
   - Grant accessibility permissions to Terminal/Python
   - Go to System Preferences → Security & Privacy → Privacy → Accessibility

3. **AppleScript execution errors**
   - Make sure Mail app is responsive
   - Try closing and reopening Mail
   - Check if Mail is processing a large number of emails

4. **No accounts found**
   - Make sure you have email accounts configured in Mail
   - Check Mail → Preferences → Accounts

5. **No messages found**
   - Verify the mailbox name is correct (case-sensitive)
   - Try using "INBOX" (all caps)
   - Check if the mailbox has messages

### Debug Mode

To see detailed AppleScript execution, you can modify the `_run_applescript` method to print the actual scripts being executed.

## 🔒 Security Notes

- The script only interacts with the Mail app through AppleScript
- No passwords or credentials are stored or transmitted
- All operations are performed through the Mail app's own interface
- The script respects Mail app's security settings

## 📝 Limitations

- **macOS only** - This script only works on macOS
- **Mail app required** - The Mail app must be running
- **AppleScript dependency** - Relies on macOS AppleScript functionality
- **UI interaction** - Some operations may be affected by Mail app's UI state
- **Performance** - AppleScript calls can be slower than direct API access

## 🚀 Advanced Usage

### Batch Operations
```python
# Process all unread messages
mail_client = MacMailClient()
if mail_client.is_mail_running():
    messages = mail_client.get_messages_from_mailbox("INBOX", 100)
    unread_messages = [msg for msg in messages if not msg['read']]
    
    for message in unread_messages:
        # Process each unread message
        print(f"Processing: {message['subject']}")
        mail_client.mark_message_as_read(message['id'])
```

### Data Export
```python
# Export all mail data to JSON
import json
from datetime import datetime

mail_client = MacMailClient()
if mail_client.is_mail_running():
    data = {
        'timestamp': datetime.now().isoformat(),
        'accounts': mail_client.get_mail_accounts(),
        'mailboxes': mail_client.get_mailboxes(),
        'unread_count': mail_client.get_unread_count(),
        'recent_messages': mail_client.get_messages_from_mailbox("INBOX", 50)
    }
    
    with open('mail_export.json', 'w') as f:
        json.dump(data, f, indent=2, default=str)
```

## 🤝 Contributing

Feel free to enhance the script with additional features:
- Email filtering and sorting
- Attachment handling
- Mail rules automation
- Integration with other macOS apps
- GUI interface

## 📄 License

This script is provided as-is for educational and personal use. 