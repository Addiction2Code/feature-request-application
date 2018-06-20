function Client(data) {
  this.id = ko.observable(data.id);
  this.name = ko.observable(data.name);
}

function ClientListViewModel() {
  // Data
  var self = this;
  self.clients = ko.observableArray([]);
  self.newClientName = ko.observable();

  // Operations
  self.addClient = function() {
  	self.save();
  	self.newClientName("");
  };

  self.deleteClient = function(id) {
    return $.ajax({
  	  url: `/api/clients/delete/${id}`,
  	  contentType: 'application/json',
  	  type: 'DELETE',
  	  success: function(data) {
        self.clients(self.clients().filter(function(obj) {
          return obj.id() !== id;
        }));
    		return;
  	  },
  	  error: function() {
  		  return console.log("Could not delete request!");
  	  }
  	});
  };

  self.save = function() {
  	return $.ajax({
  	  url: '/api/clients/new',
  	  contentType: 'application/json',
  	  type: 'POST',
  	  data: JSON.stringify({
  		  'name': self.newClientName(),
  	  }),
  	  success: function(data) {
  		self.clients.push(new Client({
        name: data.name,
        id: data.id
      }));
  		return;
  	  },
  	  error: function() {
  		  return console.log("Could not add request!");
  	  }
  	});
  };

  // Get Clients at runtime.
  $.getJSON('/api/clients', function(clientModels) {
  	var temp = $.map(clientModels.clients, function(item) {
  	  return new Client(item);
  	});
  	self.clients(temp);
  });
}

ko.applyBindings(new ClientListViewModel());
