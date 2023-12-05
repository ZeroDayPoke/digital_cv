function applyFilters() {
  let filters = {};

  $("#service-filters-form")
    .serializeArray()
    .forEach((item) => {
      filters[item.name] = item.value;
      console.log(item.name, item.value);
    });

  $("select.filter-field").each(function () {
    if (!filters[$(this).attr("name")]) {
      filters[$(this).attr("name")] = "";
    }
  });

  fetchServices(filters);
}

function fetchServices(filters) {
  console.log("Fetching services with filters:", filters);
  $.ajax({
    url: "/services?ajax=1",
    type: "GET",
    data: filters,
    success: (response) => updateServicesList(response.services),
    error: (error) => console.error("Error fetching services:", error),
  });
}

function updateServicesList(services) {
  console.log("Services:", services);
  const servicesHtml = services
    .map((service) => createServiceCard(service))
    .join("");
  $("#services-list").html(servicesHtml);
}

function createServiceCard(service) {
  const serviceDescription =
    service.details && service.details.description
      ? service.details.description
      : "No description available";

  const earlyMoverClass = service.early_eligible ? "early-mover" : "";
  const earlyMoverBanner = service.early_eligible
    ? '<button type="button" class="btn btn-outline-success btn-sm early-mover-banner">Early Mover Discount!</button>'
    : "";

  const experimentalBanner = service.experimental
    ? '<button type="button" class="btn btn-outline-danger btn-sm experimental-banner">Experimental Discount!</button>'
    : "";

  const noteButton = service.note
    ? `<button type="button" class="btn btn-sm btn-info" data-bs-toggle="tooltip" data-bs-placement="top" title="${service.note}">Note</button>`
    : "";

  const earlyMoverNote = service.early_eligible
    ? '<span class="early-mover-note">*</span>'
    : "";

  return `
    <div class="card service-card shadow-sm bg-deep-purple ${earlyMoverClass}" 
         data-category="${service.category}" 
         data-price="${service.price}" 
         data-is_available="${service.is_available}">
      <div class="card-banner-buttons position-absolute top-0 end-0 m-2">
        ${earlyMoverBanner}
        ${experimentalBanner}
      </div>
      <div class="service-image">
        <img src="${service.image_url}" alt="Image representing ${service.name}" class="img-fluid" />
      </div>
      <div class="card-body">
        <p class="card-text">${serviceDescription}</p>
        <div class="d-flex justify-content-between align-items-center">
          <div class="btn-group">
            <button type="button" class="btn btn-sm button-neon">View</button>
            <button type="button" class="btn btn-sm button-neon">Edit</button>
          </div>
          <small class="text-accent-lime-green">
            As low as ${service.price} ${service.currency}
            ${earlyMoverNote}
            ${noteButton}
          </small>
        </div>
      </div>
    </div>`;
}

function updateCheckboxButtonState(checkbox) {
  const label = checkbox.closest('label');
  const indicator = label.querySelector('.checkbox-indicator');
  if (checkbox.checked) {
    label.classList.add('btn-success');
    label.classList.remove('btn-outline-danger');
    indicator.textContent = 'Active';
  } else {
    label.classList.add('btn-outline-danger');
    label.classList.remove('btn-success');
    indicator.textContent = 'Inactive';
  }
}

$(document).ready(function () {
  applyFilters();

  $("#service-filters-form").on("submit", function (event) {
    event.preventDefault();
    applyFilters();
  });

  $(".filter-field").change(function () {
    applyFilters();
  });

  document.querySelectorAll('.btn-check').forEach(function(checkbox) {
    checkbox.addEventListener('change', function() {
      updateCheckboxButtonState(this);
      applyFilters();
    });
    updateCheckboxButtonState(checkbox);
  });
});
