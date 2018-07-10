function readURL(input) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();
    reader.onload = function(e) {
      $('#id_image').val(e.target.result);
      $('#id_src').attr('src', e.target.result);
    };

    reader.readAsDataURL(input.files[0]);
    document.getElementById('labelText').innerHTML = input.files[0].name;
  }
}
