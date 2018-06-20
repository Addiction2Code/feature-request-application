//
// Helper Functions
//

function numOrdinal(n){
  return n+(["st","nd","rd"][((n+90)%100-10)%10-1]||"th")
}

//
// Constructors
//

function ProductArea(data) {
  this.name = ko.observable(data.name);
}

function Client(data) {
  this.id = ko.observable(data.id);
  this.name = ko.observable(data.name);
  this.nextPriority = ko.observable(data.priority);
}

function FeatureRequest(data) {
  this.id = ko.observable(data.id);
  this.title = ko.observable(data.title);
  this.description = ko.observable(data.description);
  this.priority = ko.observable(data.priority);
  this.clientId = ko.observable(data.client.id);
  this.clientName = ko.observable(data.client.name);
  this.productArea = ko.observable(data.product_area);
  //this.client_name = ko.observable(data.client.name);
  /* Computed Fields */
  this.priorityText = function() {
    return numOrdinal(this.priority());
  }
}
