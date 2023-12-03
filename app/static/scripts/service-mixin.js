function applyFilters() {
  const filters = {
    category: $("#category-filter").val(),
    min_price: $("#price-filter-min").val(),
    max_price: $("#price-filter-max").val(),
    sort_order: $("#sort-filter").val(),
  };

  if ($("#availability-filter").is(":checked")) {
    filters["is_available"] = true;
  }

  $.ajax({
    url: "/services?ajax=1",
    type: "GET",
    data: filters,
    success: function (response) {
      updateServicesList(response.services);
    },
    error: function (error) {
      console.error("Error fetching services:", error);
    },
  });
}

function updateServicesList(services) {
  let servicesHtml = "";
  services.forEach((service) => {
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

    servicesHtml += `
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
  });

  $("#services-list").html(servicesHtml);
}

$(document).ready(function () {
  $(
    "#category-filter, #price-filter-min, #price-filter-max, #availability-filter, #sort-filter"
  ).change(function () {
    applyFilters();
  });
  applyFilters();
});
