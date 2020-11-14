% Copyright (c) 2006 CNRS, Laboratoire d'Acoustique Musicale (Paris)
%                          and Institut de la Communication Parl�e (Grenoble)
%
% License
%  This file is under the LGPL license,  you can
%  redistribute it and/or modify it under the terms of the GNU Lesser General 
%  Public License as published by the Free Software Foundation, either version 3 
%  of the License, or (at your option) any later version. This file is
%  distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
%  without even the implied warranty of MERCHANTABILITY or FITNESS FOR A 
%  PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
%  details.
%
% This function is part of the Covarep project: http://covarep.github.io/covarep
% 
% Author 
%  Nathalie Henrich <nathalie.henrich@gipsa-lab.fr> (April 4th, 2006)
%

function [val,ind]	=	PicDetect(s,seuil)
%PicDetect  D�tection des pics d'un signal
% 	[val,ind] = PicDetect(s,seuil) d�termine les indices et valeurs 
%	des pics pr�sents dans le signal s, � partir d'un certain
%	seuil (% du maximum de s, compris entre 0 et 1)
%	(valeur 0 par d�faut). Si n0 est pr�cis�e � la place du
%	seuil, la d�tection s'effectue � raison d'un pic par tranche de n0.

%	Auteur : Nathalie Henrich, 16/07/00.
%	$R�vision: 03/08/00, 06/09/01

if nargin == 1
   seuil = 0;
end

if seuil <= 1

% calcul de la d�riv�e et diff�rence entre signaux d�cal�s de 1
sd = diff(s);
s1 = sd(1:length(sd)-1);
s2 = sd(2:length(sd));

% d�tection des points d'inflexion
ind = find((sign(s1.*s2)==-1)&(sign(s2)<0));
ind = ind + 1;
val = s(ind);

% d�tection des pics au-dessus du seuil
indpic = find(val>=seuil*max(s));

ind = ind(indpic);
val = val(indpic);

else
  n0 = seuil;
  ind = [];
  val = [];
  [smax,indmax] = max(s(1:min([fix(3*n0/2) length(s)])));
  
  if indmax > fix(1.1*n0)
    [smax,indpic] = max(s(1:fix(1.1*n0))); 
  else
    indpic = indmax;
  end
  ind(1) = indpic;
  
  i = 1;
  while (ind(i)+fix(1.1*n0))<length(s)
    i = i+1;
    [smax,indpic] = max(s(ind(i-1)+fix(n0/2):min(length(s),ind(i-1)+fix(3*n0/2))));     
    ind(i) = indpic + ind(i-1)+fix(n0/2) -1;
  end
  
  val = s(ind);
end
