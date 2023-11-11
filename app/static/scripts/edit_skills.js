function updateEntityInstances(entityType, skillId, instanceDropdownId) {
  fetch(`/get_available_entities/${entityType}/${skillId}`)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      let options = '<option value="">Select Instance</option>';
      data.forEach((entity) => {
        options += `<option value="${entity.id}">${entity.name}</option>`;
      });
      document.getElementById(instanceDropdownId).innerHTML = options;
    })
    .catch((error) => {
      console.error("There was a problem with the fetch operation:", error);
    });
}

document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll("[id^=entityTypeSelect-]").forEach((dropdown) => {
    dropdown.addEventListener("change", function () {
      let skillIdParts = this.id.split("-");
      let skillId = skillIdParts.slice(1).join("-");
      updateEntityInstances(
        this.value,
        skillId,
        `entityInstanceSelect-${skillId}`
      );
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
  document.getElementById(elementId).textContent = levelText;
}
