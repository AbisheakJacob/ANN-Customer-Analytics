# importing the packages
from st_pages import Page, show_pages

def main():
# display the pages in the application
    show_pages(
        [
            Page("pages/model.py", "Home"),
            Page("pages/about.py", "About"),
        ]
    )

if __name__ == "__main__":
    main()