# MetaFix

MetaFix is a Python script designed to enhance the security of Windows Firewall settings. By adding specific rules, MetaFix aims to bolster network protection against potential intrusions, ensuring a more secure environment for your Windows operating system.

## Features

- **Automatic configuration**: Quickly apply a set of predefined firewall rules to block unwanted traffic.
- **Enhanced security**: Focus on blocking common intrusion points such as SMB, RDP, and FTP.
- **User-friendly**: Simple command-line interface for easy setup and execution.

## Requirements

- Python 3.x
- Administrator privileges on a Windows system

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/metafix.git
   ```
2. Navigate to the project directory:
   ```bash
   cd metafix
   ```

## Usage

Run the script with administrator privileges to apply the firewall rules:

```bash
python metafix.py
```

This script will enable the Windows Firewall and add rules to block inbound SMB and RDP traffic, as well as outbound FTP traffic.

## Important Notes

- This script must be run with administrator privileges to modify Windows Firewall settings.
- Ensure you have a backup of your current firewall settings if necessary, as this script will modify them.
- The script is tailored for a Windows environment and may not work on other operating systems.

## Contributing

Contributions are welcome! If you'd like to contribute to the project, please fork the repository and make your changes in a separate branch. Submit a pull request when your changes are ready for review.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.