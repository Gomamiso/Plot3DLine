goto draw_lines

:push_files
git add .
git commit -m "アップデート"
git push -u origin main

goto exit
:draw_lines
python plot_3d_lines.py

:exit
 
