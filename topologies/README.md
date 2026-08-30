Nested within each topology are compatible labs

Each topology is built with a management plane connecting the home lab directly to each node via SSH

sw0 in every environment creates the mgmt plane to each switch, it should be treated as an unmanaged switch. It can have an SVI for troubleshooting

configs contains the code for baking 

src will contain python to automate the entire flow