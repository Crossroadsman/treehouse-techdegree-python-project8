const sidebar_menu = document.querySelector('#sidebar-left')

sidebar_menu.addEventListener('click', (event) => {
    // If a title was clicked, identify it
    // show/hide the adjacent UL
    if (event.target.className == "sidebar-menuitem-title") {
        let adjacent = event.target.nextElementSibling
        if (adjacent.style.display === "") {
            adjacent.style.display = 'none';
        } else {
            adjacent.style.display = '';
        }
    }
});