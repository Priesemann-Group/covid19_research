function ax = sqplot()
figure('units','normalized','position',[0.3 0.3 0.3 0.5]);
ax = subplot(1,1,1);
% title(str,'interpreter','latex','FontSize',15*2)
ax.Position = [0.25 0.25 0.65 0.65];
pbaspect([1 1 1])
ax.ActivePositionProperty = 'position';
end