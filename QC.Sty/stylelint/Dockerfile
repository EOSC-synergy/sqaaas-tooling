FROM node
WORKDIR /usr/app
COPY ./ /usr/app
RUN npm install --global --save-dev --legacy-peer-deps stylelint \
                                                       stylelint-config-standard \
                                                       postcss-scss \
                                                       postcss-html \
                                                       postcss-lit
COPY stylelintrc.json /tmp/.stylelintrc.json
RUN cp /tmp/.stylelintrc.json $HOME/.stylelintrc.json
