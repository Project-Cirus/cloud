echo "Creating synapse keys & folder structure"

# Local .env
ENV_FILE=synapse.env
if [ -f "$ENV_FILE" ]; then
    # Load Environment Variables
    export $(cat "$ENV_FILE" | grep -v '#' | awk '/=/ {print $1}')

    docker-compose run --rm -e SYNAPSE_SERVER_NAME=$SYNAPSE_SERVER_NAME -e SYNAPSE_REPORT_STATS=$SYNAPSE_REPORT_STATS synapse generate

    
else
	echo "Error: Could not load ${ENV_FILE}"
	exit 1

fi
