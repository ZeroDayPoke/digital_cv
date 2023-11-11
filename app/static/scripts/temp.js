<script>
  $(document).ready(function () {
    // Display the current value for each range input
    $('input[type="range"]').each(function () {
      var displayElement = $('<span id="' + $(this).attr("id") + '_display"/>');
      $(this).after(displayElement);
      displayElement.text($(this).val());

      $(this).on("input change", function () {
        displayElement.text($(this).val());
      });
    });

    // Event listener for change on the project select field
    $("#project").change(function () {
      var projectId = $(this).val();
      if (projectId) {
        // AJAX call to get the project details
        $.ajax({
          url: "{{ url_for('project_routes.project_details', project_id='placeholder') }}".replace(
            "placeholder",
            projectId
          ),
          type: "GET",
          dataType: "json",
          success: function (data) {
            // Update form fields with the data returned
            $("#name").val(data.name);
            $("#description").val(data.description);
            $("#role").val(data.role);
            $("#repo_link").val(data.repo_link);
            $("#live_link").val(data.live_link);
            $("#misc_link").val(data.misc_link);
            $("#misc_name").val(data.misc_name);
            $("#status").val(data.status);
            $("#category").val(data.category_id);

            // Update checkboxes for related skills
            $('input[name="related_skills"]').each(function () {
              if (data.related_skills.includes(parseInt($(this).val()))) {
                $(this).prop("checked", true);
              } else {
                $(this).prop("checked", false);
              }
            });
          },
          error: function (error) {
            // Handle any errors
            console.log(error);
          },
        });
      }
    });
  });
</script>