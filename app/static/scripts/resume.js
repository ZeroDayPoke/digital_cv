$(document).ready(function () {
  let skills = [];
  $(".skill-data").each(function () {
    let skill = {
      name: $(this).data("name"),
      category: $(this).data("category"),
      level: $(this).data("level"),
      isFeatured: $(this).data("featured"),
      image: $(this).data("image"),
    };
    skills.push(skill);
  });

  let projects = [];
  $(".project-data").each(function () {
    let project = {
      name: $(this).data("name"),
      category: $(this).data("category"),
      status: $(this).data("status"),
      isFeatured: $(this).data("featured"),
      image_filename: $(this).data("image"),
      relatedSkills: $(this).data("related-skills"),
      description: $(this).data("description"),
      role: $(this).data("role"),
      repoLink: $(this).data("repo-link"),
      liveLink: $(this).data("live-link"),
    };
    projects.push(project);
  });

  function createSkillCardHtml(skill) {
    return `
    <div class="col-md-4 mb-3 skill-card">
      <h5 class="skill-name">${skill.name}</h5>
      <div class="skill-level">
        <span class="badge bg-info">${skill.level}</span>
      </div>
      <img
        src="${skill.image}"
        alt="${skill.name}"
        class="img-fluid skill-image"
      />
    </div>
    `;
  }

  function updateSkillCards(filterType, filterValue) {
    $("#skill-cards-container").empty();

    let filteredSkills = [];
    if (filterType == "category") {
      filteredSkills = skills.filter(
        (skill) => skill.category.toLowerCase() == filterValue
      );
    } else if (filterType == "level") {
      filteredSkills = skills.filter(
        (skill) => skill.level.toLowerCase() == filterValue
      );
    } else if (filterType == "featured") {
      filteredSkills = skills.filter((skill) => skill.isFeatured == "True");
      filterValue = "Featured";
    }

    $("#dynamic-header").text(
      filterValue.charAt(0).toUpperCase() + filterValue.slice(1)
    );

    filteredSkills.forEach((skill) => {
      $("#skill-cards-container").append(createSkillCardHtml(skill));
    });
  }

  $(".filter-btn").click(function () {
    let filter = $(this).data("filter");
    updateSkillCards("category", filter);
    highlightActiveFilter(".filter-btn, .level-filter-btn", this);
  });
  $(".level-filter-btn").click(function () {
    let level = $(this).data("level");
    updateSkillCards("level", level);
    highlightActiveFilter(".filter-btn, .level-filter-btn", this);
  });
  $(".filter-btn[data-is-featured='true']").click(function () {
    updateSkillCards("featured", "");
    highlightActiveFilter(".filter-btn, .level-filter-btn", this);
  });

  function createProjectCardHtml(project) {
    let skillsArray = project.relatedSkills
      .split(",")
      .map((skill) => skill.trim());
    return `
    <div class="project-card mb-5">
      <div class="row">
        <div class="col-md-8 project-image-col">
          <img src="${
            project.image_filename
          }" alt="${project.name}" class="img-fluid project-image" />
          <div class="related-skills">
            <strong>Built With:</strong>
            <ul class="list-inline">
            ${skillsArray
              .map((skill) => `<li class="list-inline-item">${skill}</li>`)
              .join("")}
          </ul>
          </div>
        </div>

        <div class="col-md-4 project-synopsis-col">
          <div class="project-synopsis">
            <h5>${project.name}</h5>
            <h6>${project.role || "N/A"}</h6>
            <p>${project.description || "Description not available"}</p>
            <div class="project-links">
              <a href="${project.repoLink || "#"}" class="btn btn-repo">Repo</a>
              <a href="${project.liveLink || "#"}" class="btn btn-live">Live</a>
            </div>
          </div>
        </div>
      </div>
    </div>`;
  }

  // Update project cards
  function updateProjectCards(filterType, filterValue) {
    $("#project-cards-container").empty();
    let filteredProjects;

    switch (filterType) {
      case "category":
        filteredProjects = projects.filter(
          (project) => project.category.toLowerCase() == filterValue
        );
        break;
      case "status":
        filteredProjects = projects.filter(
          (project) => project.status.toUpperCase() == filterValue
        );
        break;
      case "featured":
        filteredProjects = projects.filter(
          (project) => project.isFeatured == "True"
        );
        filterValue = "Featured";
        break;
    }

    $("#dynamic-project-header").text(
      filterValue.charAt(0).toUpperCase() + filterValue.slice(1)
    );
    filteredProjects.forEach((project) =>
      $("#project-cards-container").append(createProjectCardHtml(project))
    );
  }

  $(".project-filter-btn").click(function () {
    var filter = $(this).data("filter");
    var filterType = filter === "featured" ? "featured" : "category";
    updateProjectCards(filterType, filter);
    highlightActiveFilter(".project-filter-btn", this);
  });

  $(".project-status-filter-btn").click(function() {
    const status = $(this).data("status");
    updateProjectCards("status", status);
    highlightActiveFilter(".project-filter-btn, .project-status-filter-btn", this);
  });

  function highlightActiveFilter(selector, activeButton) {
    $(selector).removeClass("active-filter");
    $(activeButton).addClass("active-filter");
  }

  updateSkillCards("featured", "True");
  updateProjectCards("featured", "True");
});
