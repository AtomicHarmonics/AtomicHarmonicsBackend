#!/bin/bash
sudo mkdir -p /var/lib/backendAssets
sudo cp -a . /var/lib/backendAssets/
mkdir -p ~/.config/systemd/user/
cp ffmpegService.service flaskServer.service rtspServer.service ~/.config/systemd/user/
systemctl --user daemon-reload
systemctl --user enable rtspServer
systemctl --user enable ffmpegService
