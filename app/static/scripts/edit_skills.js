$(document).ready(function () {
  // Handler for EntityTypeSelect dropdown change
  $("[id^=entityTypeSelect-]").change(function () {
    let skillIdParts = this.id.split("-");
    let skillId = skillIdParts.slice(1).join("-");
    let entityTypeSelectId = `entityTypeSelect-${skillId}`;
    let instanceDropdownId = `entityInstanceSelect-${skillId}`;

    // Show or hide the instance dropdown based on selection
    var selectedValue = $(`#${entityTypeSelectId}`).val();
    if (selectedValue) {
      $(`#${instanceDropdownId}`).show();
    } else {
      $(`#${instanceDropdownId}`).hide();
    }

    // Fetch available entities and populate options
    $.getJSON(
      `/get_available_entities/${selectedValue}/${skillId}`,
      function (data) {
        let options = '<option value="">Select Instance</option>';
        $.each(data, function (key, entity) {
          options += `<option value="${entity.id}">${entity.name}</option>`;
        });
        $(`#${instanceDropdownId}`).html(options);
      }
    ).fail(function (error) {
      console.error("There was a problem with the fetch operation:", error);
    });
  });
});

function updateSkillLevelText(value, elementId) {
  var levelText = "Beginner";
  if (value == 2) {
    levelText = "Intermediate";
  } else if (value == 3) {
    levelText = "Advanced";
  }
  $(`#${elementId}`).text(levelText);
}
