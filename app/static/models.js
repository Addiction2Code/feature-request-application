function nth(n){
  return["st","nd","rd"][((n+90)%100-10)%10-1]||"th"
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
  //this.client_name = ko.observable(data.client.name);
  /* Computed Fields */
  this.priorityText = function() {
    return this.priority()+nth(this.priority());
  }
}
