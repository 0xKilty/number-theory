var color = sessionStorage.getItem("number-theory-color-mode") == "true"

var past_color = () => {
    console.log(sessionStorage.getItem("number-theory-color-mode"))
    set_color(sessionStorage.getItem("number-theory-color-mode") == "true")
}

function toggle_color() {
    color = !color
    set_color(color)
}

function set_color(bool) {
    sessionStorage.setItem("number-theory-color-mode", bool)
    const newColors = bool ? ["#fff", "#000", "#f3f3f3"] : ["#1e2021", "#c1c1c1", "#282a36"];
    ['background-color', 'text-color', 'hljs-background'].forEach((prop, index) => {
        document.documentElement.style.setProperty(`--${prop}`, newColors[index])
    });
}