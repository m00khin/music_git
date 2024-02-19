(function (){
    const modal = new bootstrap.Modal(document.getElementById("modal"))

    htmx.on("htmx:afterSwap", (e) => {
        // Response targeting #dialog => show the modal
        if (e.detail.target.id === "dialog") {
            modal.show()
        }
    })

    htmx.on("htmx:beforeSwap", (e) => {
        // Empty response targeting #dialog => hide the modal
        if (e.detail.target.id === "dialog" && !e.detail.xhr.response) {
            modal.hide()
            e.detail.shouldSwap = false
        }
    })

    htmx.on("hidden.bs.modal", () => {
        // Remove dialog content after hiding
        document.getElementById("dialog").innerHTML = ""
    })

})();

// (function (){
//     const modal = new bootstrap.Modal(document.getElementById("second"))
//
//     htmx.on("htmx:afterSwap", (e) => {
//         // Response targeting #dialog => show the modal
//         if (e.detail.target.id === "tracks") {
//             modal.show()
//         }
//     })
//
//     htmx.on("htmx:beforeSwap", (e) => {
//         // Empty response targeting #dialog => hide the modal
//         if (e.detail.target.id === "tracks" && !e.detail.xhr.response) {
//             modal.hide()
//             e.detail.shouldSwap = false
//         }
//     })
//
//     htmx.on("hidden.bs.modal", () => {
//         // Remove dialog content after hiding
//         document.getElementById("tracks").innerHTML = ""
//     })
//
// })();
//
