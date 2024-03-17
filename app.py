"""
Employee Management System Module

This module provides various functionalities for managing employee data, 
including adding, deleting, updating, and generating reports.
"""
from .src.menu import main_menu

def main():
    """
    Main function to start the Employee Management System.
    
    This function calls the main_menu() function to display the main menu
    of the Employee Management System to the user.
    """
    main_menu()

if __name__ == "__main__":
    main()
