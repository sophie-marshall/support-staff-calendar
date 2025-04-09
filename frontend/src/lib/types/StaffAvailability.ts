export type StaffAvailability = {
	id: number;
	firstName: string;
	lastName: string;
	availability: {
		monday: string[];
		tuesday: string[];
		wednesday: string[];
		thursday: string[];
		friday: string[];
		saturday: string[];
		sunday: string[];
	};
};
