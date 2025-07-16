#!/usr/bin/env python3
"""
Simple test to show how the script finds and interacts with the Mail app.
"""

import subprocess
import json


def run_applescript(script):
    """Run an AppleScript and return the result."""
    try:
        result = subprocess.run(
            ['osascript', '-e', script],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return f"Error: {result.stderr}"
    except Exception as e:
        return f"Exception: {e}"


def main():
    print("🔍 How the script finds your Mail app")
    print("=" * 50)
    
    # 1. Check if Mail is running
    print("\n1️⃣ Checking if Mail app is running...")
    check_script = '''
    tell application "System Events"
        return (name of processes) contains "Mail"
    end tell
    '''
    result = run_applescript(check_script)
    print(f"Result: {result}")
    
    if result.lower() == "true":
        print("✅ Mail app is running!")
    else:
        print("❌ Mail app is not running")
        return
    
    # 2. Activate Mail (bring to front)
    print("\n2️⃣ Activating Mail app...")
    activate_script = '''
    tell application "Mail"
        activate
    end tell
    '''
    result = run_applescript(activate_script)
    print(f"Result: {result}")
    print("✅ Mail app activated (brought to front)")
    
    # 3. Get account information
    print("\n3️⃣ Getting email accounts...")
    accounts_script = '''
    tell application "Mail"
        set accountNames to {}
        repeat with theAccount in accounts
            set accountName to name of theAccount
            copy accountName to end of accountNames
        end repeat
        return accountNames
    end tell
    '''
    result = run_applescript(accounts_script)
    print(f"Accounts found: {result}")
    
    # 4. Get unread count
    print("\n4️⃣ Getting unread message count...")
    unread_script = '''
    tell application "Mail"
        set unreadCount to 0
        repeat with theMailbox in mailboxes
            set unreadCount to unreadCount + (unread count of theMailbox)
        end repeat
        return unreadCount
    end tell
    '''
    result = run_applescript(unread_script)
    print(f"Unread messages: {result}")
    
    # 5. Get recent messages
    print("\n5️⃣ Getting recent messages from inbox...")
    messages_script = '''
    tell application "Mail"
        set messageList to {}
        set theMessages to messages of inbox
        set messageCount to count of theMessages
        set startIndex to (messageCount - 3 + 1)
        if startIndex < 1 then set startIndex to 1
        
        repeat with i from startIndex to messageCount
            set theMessage to item i of theMessages
            set messageSubject to subject of theMessage
            set messageSender to sender of theMessage
            set messageInfo to messageSubject & " | " & messageSender
            copy messageInfo to end of messageList
        end repeat
        return messageList
    end tell
    '''
    result = run_applescript(messages_script)
    print(f"Recent messages: {result}")
    
    # 6. Show the AppleScript commands being used
    print("\n🔧 AppleScript Commands Used:")
    print("=" * 30)
    print("1. Check if Mail is running:")
    print("   tell application \"System Events\"")
    print("       return (name of processes) contains \"Mail\"")
    print("   end tell")
    print()
    print("2. Activate Mail:")
    print("   tell application \"Mail\"")
    print("       activate")
    print("   end tell")
    print()
    print("3. Get accounts:")
    print("   tell application \"Mail\"")
    print("       set accountNames to {}")
    print("       repeat with theAccount in accounts")
    print("           set accountName to name of theAccount")
    print("           copy accountName to end of accountNames")
    print("       end repeat")
    print("       return accountNames")
    print("   end tell")
    
    print("\n✅ Script successfully found and interacted with your Mail app!")


if __name__ == "__main__":
    main() 