function FeatureRequest(data) {
  this.id = ko.observable(data.id);
  this.title = ko.observable(data.title);
  this.description = ko.observable(data.description);
}

function FeatureRequestListViewModel() {
  // Data
  var self = this;
  self.featureRequests = ko.observableArray([]);
  self.newFeatureRequestTitle = ko.observable();
  self.newFeatureRequestDesc = ko.observable();

  // Operations
  self.addFeatureRequest = function() {
  	self.save();
  	self.newFeatureRequestTitle("");
  	self.newFeatureRequestDesc("");
  };

  self.save = function() {
  	return $.ajax({
  	  url: '/feature-requests/new',
  	  contentType: 'application/json',
  	  type: 'POST',
  	  data: JSON.stringify({
  		  'title': self.newFeatureRequestTitle(),
  		  'description': self.newFeatureRequestDesc()
  	  }),
  	  success: function(data) {
  		self.featureRequests.push(new FeatureRequest({
        title: data.title,
        description: data.description, id: data.id
      }));
  		return;
  	  },
  	  error: function() {
  		  return console.log("Could not add request!");
  	  }
  	});
  };

  // Get Feature Requests at runtime.
  $.getJSON('/feature-requests', function(featureRequestModels) {
  	var temp = $.map(featureRequestModels.feature_requests, function(item) {
  	  return new FeatureRequest(item);
  	});
  	self.featureRequests(temp);
  });
}

ko.applyBindings(new FeatureRequestListViewModel());
