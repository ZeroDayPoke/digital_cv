$(document).ready(function() {
  $("[id^=entityTypeSelect-]").change(function() {
    let skillIdParts = this.id.split("-");
    let skillId = skillIdParts.slice(1).join("-");
    let instanceDropdownId = `entityInstanceSelect-${skillId}`;

    $.getJSON(`/get_available_entities/${this.value}/${skillId}`, function(data) {
      let options = '<option value="">Select Instance</option>';
      $.each(data, function(key, entity) {
        options += `<option value="${entity.id}">${entity.name}</option>`;
      });
      $(`#${instanceDropdownId}`).html(options);
    }).fail(function(error) {
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
