FROM ollama/ollama:0.3.6

# Listen on all interfaces, port 8080
ENV OLLAMA_HOST 0.0.0.0:8080

# Store model weight files in /models
ENV OLLAMA_MODELS /models

# Reduce logging verbosity
ENV OLLAMA_DEBUG false

# Never unload model weights from the GPU
ENV OLLAMA_KEEP_ALIVE -1

# If you want to deploy your own AI model from your local machine, uncomment below to copy your model files to the /models directory
# COPY path/to/your/model/files /models

# Store the model weights in the container image
# Change the model name to your own AI model
ENV MODEL gemma2:9b         
RUN ollama serve & sleep 5 && ollama pull ${MODEL}

# Start Ollama
ENTRYPOINT ["ollama", "serve"]