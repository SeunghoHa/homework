function order_btn() {
    if (confirm("작성하신 내용으로 주문하시겠습니까?") == true) {
        // 여기에 DB로 저장하는 기능 구현
        if ($("#customerName").val() === '') {
            alert("성함을 입력해주세요.");
            $("#customerName").focus();
        } else if ($("#itemCount option:selected").val() == 0) {
            alert("수량을 입력해주세요.");
            $("#itemCount").focus();
        } else if ($("#customerAddress").val() === '') {
            alert("주소를 입력해주세요.");
            $("#customerAddress").focus();
        } else if ($("#customerNumber").val() === '') {
            alert("전화번호를 입력해주세요.");
            $("#customerNumber").focus();
        } else {
            alert("주문이 완료되었습니다!");
        }
    } else {
        return false;
    }
}