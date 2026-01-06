FROM nginx:alpine

# Remove default nginx page
RUN rm -rf /usr/share/nginx/html/*

# Copy our frontend code
COPY index.html /usr/share/nginx/html/index.html

EXPOSE 80
