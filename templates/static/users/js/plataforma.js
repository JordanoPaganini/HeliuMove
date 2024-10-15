let sidebar = document.querySelector(".sidebar");
let closeBtn = document.querySelector("#btn");
let searchBtn = document.querySelector(".bx-search");

closeBtn.addEventListener("click", ()=>{
    sidebar.classList.toggle("open");
    menuBtnChange();
});

searchBtn.addEventListener("click", ()=>{ 
    sidebar.classList.toggle("open");
    menuBtnChange();
});

function exportar() {
    const currentUrl = window.location.pathname;
    
    if (currentUrl.includes('/sistemas/')) {
        const slug = currentUrl.split('/sistemas/')[1];
        
        window.location.href = `/sistemas/export/${slug}`;
    } else {
        console.error('Slug não encontrado na URL.');
    }
}

function menuBtnChange() {
if(sidebar.classList.contains("open")){
    closeBtn.classList.replace("bx-menu", "bx-menu-alt-right");
}else {
    closeBtn.classList.replace("bx-menu-alt-right","bx-menu");
}
};