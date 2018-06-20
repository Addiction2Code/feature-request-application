function FeatureRequestListViewModel() {

  //
  // Data
  //

  var self = this;
  self.clients = ko.observableArray([]);
  self.curClient = ko.observable();
  self.curDragItem = ko.observable();
  self.finDragItem = ko.observable();
  self.featureRequests = ko.observableArray([]);
  self.newFeatureRequestTitle = ko.observable();
  self.newFeatureRequestDesc = ko.observable();
  self.newFeatureRequestTargetDate = ko.observable(new Date().toISOString().split('T')[0]);
  self.newFeatureRequestPriority = ko.observable();
  self.newFeatureRequestClient = {
    options: ko.observableArray(["Loading..."]),
    selectedId: ko.observable("None"),
    selectedName: ko.observable("None")
  };

  // Statically set ProductAreas for now.
  self.newFeatureRequestProductArea = {
    options: ko.observableArray([
      new ProductArea({"name": "Policies"}),
      new ProductArea({"name": "Billing"}),
      new ProductArea({"name": "Claims"}),
      new ProductArea({"name": "Reports"})
    ]),
    selectedId: ko.observable()
  };


  //
  // Init Related Functions
  //

  // Handle Drag and Drop functionality.
  self.initDragDrop = function() {
    // Initialise the table
    $("#mainTable").tableDnD({
      onDragStart: function(table, row) {
        // Store "Drag From" location.
        self.curDragItem(null);
        self.curDragItem($(row).index()+1);
      },
      onDrop: function(table, row) {
        // Store "Drag To" location.
        self.finDragItem(null);
        self.finDragItem($(row).index()+1);
        // Tell the server to reprioritize requests between the given params.
        return $.ajax({
          url: '/api/feature-requests/prioritize',
          contentType: 'application/json',
          type: 'POST',
          data: JSON.stringify({
            'client_id': self.curClient().id(),
            'cur_priority': self.curDragItem(),
            'new_priority': self.finDragItem(),
          }),
          success: function(data) {
            self.updateFeatureRequests(data.feature_requests);
            self.initDragDrop();
            $('[data-toggle="tooltip"]').tooltip();
            return;
          },
          error: function() {
            return console.log("Could not delete request!");
          }
        });
      }
    });
  };

  self.initTableFeatures = function() {
    self.initDragDrop();
    $(function () {
      $('[data-toggle="tooltip"]').tooltip();
    });
  }


  //
  // Operations
  //

  self.displayFriendlyDate = function(date) {
    d = new Date(date);
    return (d.getUTCMonth()+1)+'/'+(d.getUTCDate())+'/'+(d.getUTCFullYear());
  }

  // Save and clear data.
  self.addFeatureRequest = function() {
  	self.saveNewFeatureRequest();
  	self.newFeatureRequestTitle("");
  	self.newFeatureRequestDesc("");
  	self.newFeatureRequestPriority("");
  	self.newFeatureRequestClient.options();
    self.newFeatureRequestClient.selectedId();
  };

  // Update and reprioritize data hence table.
  self.updateFeatureRequests = function(updates) {
    var data = self.featureRequests();
    data.valueHas
    for(var a = 0; a < updates.length; a++) {
      var objFound = false;
      for (var i = 0; i < data.length; i++) {
        if(updates[a].id === data[i].id()) {
          objFound = true;
          data[i] = new FeatureRequest(updates[a]);
        }
      }
      if(!objFound){
        data.push(new FeatureRequest(updates[a]));
      }
    }
    self.featureRequests(data);
    self.initTableFeatures();
  };

  self.setCurClient = function(client) {
    return self.curClient(client);
  }


  //
  // API Related Functions
  //

  // Delete and reprioritize data hence table.
  self.deleteFeatureRequest = function(id) {
    return $.ajax({
  	  url: `/api/feature-requests/delete/${id}`,
  	  contentType: 'application/json',
  	  type: 'DELETE',
  	  success: function(data) {
        self.featureRequests(self.featureRequests().filter(function(obj) {
          return obj.id() !== id;
        }));
        self.updateFeatureRequests(data.feature_requests);
    		return;
  	  },
  	  error: function() {
  		  return console.log("Could not delete request!");
  	  }
  	});
  };

  // Save and reprioritize data hence table.
  self.saveNewFeatureRequest = function() {
  	return $.ajax({
  	  url: '/api/feature-requests/new',
  	  contentType: 'application/json',
  	  type: 'POST',
  	  data: JSON.stringify({
  		  'title': self.newFeatureRequestTitle(),
        'product_area': self.newFeatureRequestProductArea.selectedId(),
        'target_date': self.newFeatureRequestTargetDate(),
  		  'description': self.newFeatureRequestDesc() ? self.newFeatureRequestDesc() : '',
        'priority': parseInt(self.newFeatureRequestPriority()),
        'client_id': self.newFeatureRequestClient.selectedId(),
  	  }),
  	  success: function(data) {
        self.updateFeatureRequests(data.feature_requests);
    		return;
  	  },
  	  error: function() {
  		  return console.log("Could not add request!");
  	  }
  	});
  };


  self.curClient(new Client(window.FeatureHandler.client));
  self.newFeatureRequestClient.selectedId(self.curClient().id());

  // Get Feature Requests at runtime.
  $.getJSON(`/api/feature-requests/${self.curClient().id()}`, function(featureRequestModels) {
  	var temp = $.map(featureRequestModels.feature_requests, function(item) {
  	  return new FeatureRequest(item);
  	});
  	self.featureRequests(temp);
  });

  // Get Clients at runtime.
  $.getJSON('/api/clients', function(clientModels) {
    var temp = $.map(clientModels.clients, function(item) {
      return new Client(item);
    });
    self.clients(temp);
    self.newFeatureRequestClient.options(temp);
  });

  // Initialize Drag Drop and Tooltip (Details)
  $(document).ready(function() {
    self.initTableFeatures();
  });

}

ko.applyBindings(new FeatureRequestListViewModel());
