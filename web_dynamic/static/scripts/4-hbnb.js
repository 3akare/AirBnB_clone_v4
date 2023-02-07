$('document').ready(function () {
  const amenities = {};
  $('INPUT[type="checkbox"]').change(function () {
    if ($(this).is(':checked')) {
      amenities[$(this).attr('data-id')] = $(this).attr('data-name');
    } else {
      delete amenities[$(this).attr('data-id')];
    }
    $('#list').text(Object.values(amenities).join(', '));
  });
  $.get('http://127.0.0.1:5001/api/v1/status/', function (data) {
    if (data.status === 'OK') {
      $('#api_status').addClass('available');
    }
  });

  $.ajax({
    url: 'http://127.0.0.1:5001/api/v1/places_search/',
    type: 'POST',
    data: '{}',
    dataType: 'json',
    contentType: 'application/json',
    success: appendPlaces
  });
  $('BUTTON').on('click', () => {
    console.log('david');
    $.ajax({
      url: 'http://127.0.0.1:5001/api/v1/places_search/',
      type: 'POST',
      data: JSON.stringify({ amenities: Object.keys(amenities) }),
      dataType: 'json',
      contentType: 'application/json',
      success: appendPlaces
    });
  });
  function appendPlaces (data) {
    data.forEach(place => {
      $('DIV.article').empty();
      $('DIV.article').append(`
            <article>
            <div class="new-flex">
                <h2> ${place.name}</h2>
                <div class="price_by_night">
                    <p> ${place.prices_by_night} </p>
                </div>
            </div>
            <div class="information">
                <div class="new-flex">
                    <div class="max_guest">
                        <img src="../static/styles/static/max-guest.png" alt="">
                        <p> ${place.max_guest} Guests</p>
                    </div>
                    <div class="number_rooms">
                        <img src="../static/styles/static/icon_bed.png" alt="">
                        <p>${place.number_of_rooms} Bedroom</p>
                    </div>
                    <div class="number_bathrooms">
                        <img src="../static/styles/static/icon_bath.png" alt="">
                        <p>${place.number_of_bathrooms} Bathroom</p>
                    </div>
                </div>
                <div class="user">
                    <p>
                        <strong>Owner</strong>
                        ${place.owner}
                    </p>
                </div>
                <div class="description">
                    <p>
                        ${place.description}
                    </p>
                </div>
            </div>
        </article>
            `);
    });
  }
});
