FROM soothemade-render-preview
RUN apt-get update && apt-get install -y --no-install-recommends pandoc imagemagick && rm -rf /var/lib/apt/lists/*
