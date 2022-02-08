#!/bin/bash
# TODO(@brandon) remove print of experimentalist name when typing
echo Hello, who am I talkign to?
read experimentalist_name
sleep 0.9
echo Hello, $experimentalist_name this is Brandon. Welcome to The Matrix. 
sleep 0.9
echo Let\'s start an experiment.
read -p "Name of the fridge: " fridge_name
sleep 0.9
read -p "Name of the device: " device_name
read -p "Name of the experiment: "

# Create function to make lower case and remove spaces
function strip_down {
	lower_str=$($1 | tr '[:upper:]' '[:lower:]')
	no_space=${lower_str// /_}

}
fridge_name = strip_down "$fridge_name"
date_today=$(date +%Y%m%d_%s) 
echo "$date_today $fridge_name $device_name"
