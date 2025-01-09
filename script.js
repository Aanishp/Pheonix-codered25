// Get the current page's file name (e.g., "home.html")
const currentPage = window.location.pathname.split("/").pop();

// Select all navigation links
const navLinks = document.querySelectorAll(".navigation a");

// Loop through the links and add the 'active' class to the matching link
navLinks.forEach(link => {
    const linkPath = link.getAttribute("href");
    if (linkPath === currentPage || (currentPage === "" && linkPath === "home.html")) {
        link.classList.add("active");
    }
});