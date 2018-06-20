// creating Knockoutjs object that binds data of form, dynamically which the user enters

  var appViewModel =  {                 
    title:ko.observable(""),
    description:ko.observable(""),
    client:ko.observable(""),
    clientPriority:ko.observable(""),
    targetDate:ko.observable(""),
    productArea:ko.observable("")
  };
  self.Done = function () {
    console.log("After clicking submit");
    var jsonData = ko.toJSON(appViewModel);
    console.log("converting knockout.js data to json data " + jsonData);

    $.ajax({
      url: '/postdata',
      type: 'POST',
      data: jsonData,
      contentType: 'application/json',
      success: function (result) {
        alert("Record inserted Sucessfully");

      },
      error: function (XMLHttpRequest, textStatus, errorThrown) {

        alert("some error");
      }
    });
  };

  ko.applyBindings(appViewModel);
