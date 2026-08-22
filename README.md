# Update Termux packages
pkg update && pkg upgrade -y

# Install required dependencies
pkg install python git -y

# Clone the repository
git clone https://github.com/riyad-sh/Zeem.git

# Enter the project directory
cd ZeeM

# Run ZeeM
python zeem.py
