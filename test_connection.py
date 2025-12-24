"""
MySQL Connection Diagnostic Tool for XAMPP
This script helps identify connection issues with your XAMPP MySQL database
"""

import mysql.connector as mysql
from mysql.connector import Error


def test_connection(port=3306):
    """Test MySQL connection with given port"""
    config = {
        'host': 'localhost',
        'user': 'root',
        'password': '',
        'port': port,
        'auth_plugin': 'mysql_native_password',
        'connection_timeout': 3  # 3 second timeout
    }
    
    print(f"\n{'='*60}")
    print(f"Testing connection on port {port}...")
    print(f"{'='*60}")
    
    try:
        connection = mysql.connect(**config)
        
        if connection.is_connected():
            db_info = connection.get_server_info()
            cursor = connection.cursor()
            cursor.execute("SELECT VERSION()")
            version = cursor.fetchone()
            
            print(f"✅ SUCCESS! Connected to MySQL Server")
            print(f"   Server Version: {db_info}")
            print(f"   MySQL Version: {version[0]}")
            print(f"   Host: {config['host']}")
            print(f"   Port: {config['port']}")
            print(f"   User: {config['user']}")
            
            # Test database operations
            cursor.execute("SHOW DATABASES")
            databases = cursor.fetchall()
            print(f"\n   Available databases: {len(databases)}")
            for db in databases[:5]:  # Show first 5
                print(f"   - {db[0]}")
            
            connection.close()
            return True
            
    except Error as e:
        print(f"❌ FAILED to connect on port {port}")
        print(f"   Error Code: {e.errno}")
        print(f"   Error Message: {e.msg}")
        return False
    
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False


def main():
    print("\n" + "="*60)
    print("XAMPP MySQL Connection Diagnostic Tool")
    print("="*60)
    
    # Test common ports
    ports_to_test = [3306, 3307, 3308]
    successful_port = None
    
    for port in ports_to_test:
        if test_connection(port):
            successful_port = port
            break
    
    print("\n" + "="*60)
    print("DIAGNOSTIC RESULTS")
    print("="*60)
    
    if successful_port:
        print(f"✅ MySQL is running on port {successful_port}")
        print(f"\nYour database.py is configured for port 3306")
        if successful_port != 3306:
            print(f"⚠️  WARNING: MySQL is running on port {successful_port}, not 3306!")
            print(f"   Update the 'port' value in database.py to {successful_port}")
    else:
        print("❌ Could not connect to MySQL on any common port")
        print("\n📋 TROUBLESHOOTING STEPS:")
        print("   1. Open XAMPP Control Panel")
        print("   2. Click 'Start' button next to MySQL")
        print("   3. Check if MySQL shows 'Running' status")
        print("   4. Click 'Config' → 'my.ini' to check the port number")
        print("   5. Look for 'port=' under [mysqld] section")
        print("   6. Make sure no other program is using port 3306")
        print("\n📌 Common Issues:")
        print("   - MySQL service not started in XAMPP")
        print("   - Port 3306 blocked by firewall")
        print("   - Another MySQL instance running")
        print("   - XAMPP installation corrupted")
    
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
