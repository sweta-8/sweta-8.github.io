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

function nextTab(currentSectionId) {
    var menuItems = document.querySelectorAll('#sidebar-menu li a');
    for (var i = 0; i < menuItems.length; i++) {
        if (menuItems[i].getAttribute('href').substring(1) === currentSectionId) {
            var nextIndex = (i + 1) % menuItems.length;
            var nextSectionId = menuItems[nextIndex].getAttribute('href').substring(1);
            showContent(nextSectionId);
            break;
        }
    }
}