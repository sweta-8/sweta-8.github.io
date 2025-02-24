function showContent(sectionId) {
    // Hide all content sections
    var sections = document.querySelectorAll('.content-section');
    sections.forEach(function(section) {
        section.style.display = 'none';
    });

    // Show the selected content section
    var selectedSection = document.getElementById(sectionId);
    selectedSection.style.display = 'block';
}