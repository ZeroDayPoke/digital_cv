// ./app/static/scripts/pet.js
$(document).ready(function () {
  let imageIndex = $("#image-fields-container .image-container").length;

  $("#add-image-button").click(function () {
    var newFieldHtml = `
          <div class="mb-3 image-container">
              <input type="file" name="images-${imageIndex}-image" class="form-control mb-2" placeholder="Choose Image">
              <input type="text" name="images-${imageIndex}-description" class="form-control" placeholder="Image Description">
              <button type="button" class="remove-image-btn btn btn-danger">Remove</button>
          </div>
      `;
    $("#image-fields-container").append(newFieldHtml);
    imageIndex++;
  });

  $(".remove-image-btn").click(function () {
    var filename = $(this)
      .siblings('input[type="hidden"][name$="filename"]')
      .val();
    $("<input>")
      .attr({
        type: "hidden",
        name: "remove_images",
        value: filename,
      })
      .appendTo("form");
    $(this).closest(".image-container").remove();
  });
});
