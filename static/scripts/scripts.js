function copy_button() {
    const paragraph = document.getElementById('new-password');
    const text = paragraph.innerText;

    const textarea = document.createElement('textarea');
    textarea.value = text;
    document.body.appendChild(textarea);

    textarea.select();
    document.execCommand('copy');
    document.body.removeChild(textarea);


}

function pagebutton() {
    window.location.href = 'https://www.washingtonpost.com/technology/2023/05/04/passwords-tips-privacy/';
}