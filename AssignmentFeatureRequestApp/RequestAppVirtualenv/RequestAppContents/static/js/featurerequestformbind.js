var formViewModel = {
  title: ko.observable(""),
  description: ko.observable(""),
  client: ko.observable(""),
  clientPriority: ko.observable(""),
  targetDate: ko.observable(""),
  productArea: ko.observable("")
};
//creating function for submit to perform some action after clicking submit button.
self.onSubmit = function () {
  console.log("After clicking submit");
  //converting knockout.js object into json data.
  $.ajax({
    url: '/createFeature',
    type: 'POST',
    data: ko.toJSON(formViewModel),
    contentType: 'application/json',
    success: function (result) {
      // Giving alerts according to result variable
      if (result == "successfully inserted data into database") {
        alert("Record inserted Sucessfully");
        window.location = '/table';
      }
      else {
        alert(result + "please contact your administrator");
      }
    },
    error: function (XMLHttpRequest, textStatus, errorThrown) {
      alert("Error Occured. Please contact your administrator");
    }
  });
};
// Below script is used to restrict the target date to only display future dates starting current day.
var now = new Date(),
  stringDate = now.toISOString();
minDate = stringDate.substring(0, 10);
$('#target').prop('min', minDate);
ko.applyBindings(formViewModel);