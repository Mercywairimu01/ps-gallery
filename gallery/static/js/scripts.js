document.addEventListener('DOMContentLoaded', function () {
    const button = document.querySelectorAll("[data-target]");
    const repl = document.querySelectorAll(".close-modal");
    const overlay = document.getElementById("overlay");
    const textcopy = document.querySelectorAll('.copylink')
    const btncopy = document.querySelectorAll('.btncopy')
  
    button.forEach((btn) => {
      btn.addEventListener("click", () => {
        document.querySelector(btn.dataset.target).classList.add("active");
        overlay.classList.add("active");
      });
    });
  
    repl.forEach((btn) => {
      btn.addEventListener("click", () => {
        const modal = btn.closest(".modal");
        modal.classList.remove("active");
        overlay.classList.remove("active");
      });
    });
  
    window.onclick = (event) => {
      if (event.target == overlay) {
        const modals = document.querySelectorAll(".modal");
        modals.forEach((modal) => modal.classList.remove("active"));
        overlay.classList.remove("active");
      }
    };
  
    textcopy.forEach((btn, i) => {
      btncopy[i].addEventListener("click", ()=>{
        link = btn.id.split("copyl");
        var copytext = document.getElementById('copyl'+link[1])
        copytext.select()      
        copytext.setSelectionRange(0, 99999)
        document.execCommand('copy')
        alert("Copied link: " + copytext.value);
      })
    });
  })