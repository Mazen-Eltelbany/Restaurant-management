function Setphone() {
    var select = document.getElementById("cust_name");
    var phone = select.options[select.selectedIndex].getAttribute("data-phone");
    document.getElementById("phone").value = phone;
}
