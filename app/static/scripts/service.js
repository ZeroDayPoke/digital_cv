$(document).ready(function () {
  $('[data-bs-toggle="tooltip"]').tooltip();
});

function applyFilters() {
  var categoryFilter = $("#category-filter").val();
  var minPriceFilter = parseFloat($("#price-filter-min").val()) || 0;
  var maxPriceFilter = parseFloat($("#price-filter-max").val()) || Infinity;
  var sortValue = $("#sort-filter").val();
  var availabilityChecked = $("#availability-filter").is(":checked");
  var serviceContainer = $(".row.row-cols-1.row-cols-sm-2.row-cols-md-3.g-3");
  var allServices = $(".service-card").toArray();

  // Filter Logic
  services = allServices.filter(function (service) {
    var price = parseFloat($(service).data("price"));
    var category = $(service).data("category");
    var isAvailable = $(service).data("is_available") === "True";

    return (
      (!categoryFilter || category === categoryFilter) &&
      price >= minPriceFilter &&
      price <= maxPriceFilter &&
      (!availabilityChecked || isAvailable)
    );
  });

  // Sorting Logic
  if (sortValue) {
    services.sort(function (a, b) {
      var priceA = parseFloat($(a).data("price"));
      var priceB = parseFloat($(b).data("price"));
      console.log(priceA, priceB);
      return sortValue === "asc" ? priceA - priceB : priceB - priceA;
    });
  }

  serviceContainer.empty();

  $(services).each(function() {
    serviceContainer.append(this);
  });

  if (services.length === 0) {
    serviceContainer.html(
      '<p class="text-center">No services found for your criteria.</p>'
    );
  }
}
