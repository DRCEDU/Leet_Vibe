# Email Reader Script

A comprehensive Python script to read emails from various email providers via IMAP. This script can connect to your Mail client's email accounts and read, search, and manage emails programmatically.

## Features

- ✅ Connect to Gmail, Outlook, Yahoo, and other IMAP-compatible email services
- ✅ Read recent emails, unread emails, and search emails
- ✅ Parse email content including subject, sender, body, and attachments
- ✅ Save emails to JSON format for further processing
- ✅ Mark emails as read/unread
- ✅ Delete emails
- ✅ List and navigate email folders
- ✅ Command-line interface with various options

## Prerequisites

### For Gmail Users
1. **Enable 2-Factor Authentication** on your Google account
2. **Generate an App Password**:
   - Go to Google Account settings
   - Security → 2-Step Verification → App passwords
   - Generate a password for "Mail"
   - Use this app password instead of your regular password

### For Outlook/Hotmail Users
1. **Enable 2-Factor Authentication** (recommended)
2. **Generate an App Password** (if 2FA is enabled)
3. Or use your regular password (if 2FA is disabled)

### For Yahoo Users
1. **Enable 2-Factor Authentication**
2. **Generate an App Password**:
   - Account Security → Generate app password
   - Use this app password

## Installation

No external dependencies required! The script uses only Python built-in libraries.

```bash
# Clone or download the script files
cd programming-languages/python/

# Make the script executable (optional)
chmod +x email_reader.py
chmod +x email_reader_example.py
```

## Usage

### Method 1: Interactive Mode (Recommended for beginners)

```bash
python email_reader.py
```

This will prompt you for:
- Email address
- Password (hidden input)
- Then show available folders and recent emails

### Method 2: Command Line Interface

```bash
# Basic usage - read recent emails
python email_reader.py --email your.email@gmail.com --limit 10

# Read unread emails only
python email_reader.py --email your.email@gmail.com --unread --limit 5

# Search for specific emails
python email_reader.py --email your.email@gmail.com --search "FROM someone@example.com" --limit 10

# Save emails to JSON file
python email_reader.py --email your.email@gmail.com --save my_emails.json --limit 20

# Specify email provider
python email_reader.py --email your.email@outlook.com --provider outlook --limit 5

# Read from specific folder
python email_reader.py --email your.email@gmail.com --folder "Sent" --limit 10
```

### Method 3: Use the Example Script

```bash
python email_reader_example.py
```

This provides an interactive guided experience with all features.

## Command Line Options

| Option | Description | Example |
|--------|-------------|---------|
| `--email` | Email address (required) | `--email user@gmail.com` |
| `--password` | Password (will prompt if not provided) | `--password mypassword` |
| `--provider` | Email provider (auto/gmail/outlook/yahoo) | `--provider gmail` |
| `--folder` | Email folder to read | `--folder "INBOX"` |
| `--limit` | Number of emails to read | `--limit 10` |
| `--search` | IMAP search criteria | `--search "FROM john@example.com"` |
| `--unread` | Only read unread emails | `--unread` |
| `--save` | Save emails to JSON file | `--save emails.json` |

## IMAP Search Criteria Examples

You can use various IMAP search criteria:

```bash
# Search by sender
--search "FROM someone@example.com"

# Search by subject
--search "SUBJECT important"

# Search by date
--search "SINCE 01-Jan-2024"

# Search unread emails from specific sender
--search "UNSEEN FROM someone@example.com"

# Search emails with attachments
--search "HEADER Content-Type multipart/mixed"

# Search emails larger than 1MB
--search "LARGER 1048576"
```

## Using the EmailReader Class in Your Code

```python
from email_reader import EmailReader

# Create email reader
reader = EmailReader("your.email@gmail.com", "your_password")

# Connect to server
if reader.connect():
    try:
        # Select INBOX
        reader.select_folder("INBOX")
        
        # Get recent emails
        emails = reader.get_recent_emails(5)
        
        # Process emails
        for email_data in emails:
            print(f"Subject: {email_data['subject']}")
            print(f"From: {email_data['from']}")
            print(f"Body: {email_data['body'][:100]}...")
            
    finally:
        reader.disconnect()
```

## Email Data Structure

Each email is returned as a dictionary with the following structure:

```python
{
    'subject': 'Email subject',
    'from': 'sender@example.com',
    'to': 'recipient@example.com',
    'date': 'Wed, 15 Jan 2024 10:30:00 +0000',
    'body': 'Email body text...',
    'attachments': [
        {
            'filename': 'document.pdf',
            'content_type': 'application/pdf',
            'size': 1024000
        }
    ],
    'id': '12345'  # Email ID (only when returned from search methods)
}
```

## Troubleshooting

### Connection Issues

1. **"Authentication failed"**:
   - For Gmail: Use an App Password instead of your regular password
   - For Outlook: Enable "Less secure app access" or use App Password
   - For Yahoo: Use an App Password

2. **"Connection timeout"**:
   - Check your internet connection
   - Verify the email provider's IMAP server is correct
   - Try using a different network

3. **"SSL certificate error"**:
   - This is rare but can happen with corporate networks
   - Contact your IT department

### Common Issues

1. **No emails found**:
   - Check if the folder name is correct (case-sensitive)
   - Verify your email account has emails
   - Try using "INBOX" (all caps)

2. **Script hangs**:
   - Large email accounts may take time to process
   - Use `--limit` to restrict the number of emails
   - Check your internet connection

## Security Notes

- The script stores passwords in memory only during execution
- Passwords are not saved to disk
- Use App Passwords instead of your main password when possible
- The script uses SSL/TLS encryption for all connections

## Examples

### Read and save recent emails
```bash
python email_reader.py --email user@gmail.com --limit 20 --save recent_emails.json
```

### Search for emails from a specific sender
```bash
python email_reader.py --email user@gmail.com --search "FROM boss@company.com" --limit 50
```

### Get all unread emails
```bash
python email_reader.py --email user@gmail.com --unread
```

### Read emails from a specific date
```bash
python email_reader.py --email user@gmail.com --search "SINCE 01-Jan-2024" --limit 100
```

## Contributing

Feel free to enhance the script with additional features:
- Email composition and sending
- Attachment downloading
- Email filtering and sorting
- Integration with other email services
- GUI interface

## License

This script is provided as-is for educational and personal use. 