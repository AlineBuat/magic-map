% Read image
[I,m] = imread('iteration31.png');
% Find purple-ish colors
mask1 = abs(m(:,3)-m(:,1))<0.8;
mask2 = abs(m(:,3)-m(:,2))>0.3;
mask3 = abs(m(:,2)-m(:,1))>0.3;
mask = mask1 & mask2 & mask3;
% Convert purple-ish colors to green-ish colors
m(mask,:) = 1-m(mask,:);
% Create and show newly colored image
rgb = ind2rgb(I,m);
imshow(rgb);