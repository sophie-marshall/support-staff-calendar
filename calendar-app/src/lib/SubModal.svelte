<script lang="ts">
	// import custom types
	import type { StaffAvailability } from './types/StaffAvailability';

	// import child components
	import SubForm from './SubForm.svelte';

	// set prop for callback
	export let setShowSubModal: (value: boolean) => void;

	// instanatite vars for component
	let availableStaff: StaffAvailability[] = [];
	let showResults: boolean = false;
	let headerText: string = "Let's get the details";
	let selectedStaffMember: string = '';
	let showConfirmation: boolean = false;
	let confirmationMessage: string = '';

	// handle callbacks
	function handleFoundStaff(staff: StaffAvailability[]) {
		availableStaff = staff;
	}
	function handleSetShowResults(value: boolean) {
		showResults = value;
		headerText = 'Please select an available team member:';
		selectedStaffMember = '';
	}

	// button handlers
	function handleSubOptionClick(subName: string) {
		if (selectedStaffMember === subName) {
			selectedStaffMember = '';
		} else {
			selectedStaffMember = subName;
		}
	}

	function handleRequestSub(subName: string) {
		showConfirmation = !showConfirmation;
		if (showConfirmation === true) {
			confirmationMessage = `We will notify you once ${subName} responds.`;
		}
		headerText = 'Request sent! 🚀';

		setTimeout(() => {
			setShowSubModal(false);
		}, 2500);
	}
</script>

<div class="sub-modal">
	<h4>{headerText}</h4>
	<div class="modal-contents">
		<div class="form-container" style={showResults ? 'display: none' : 'display: flex'}>
			<SubForm
				availableStaff={handleFoundStaff}
				{setShowSubModal}
				setShowResults={handleSetShowResults}
			/>
		</div>
		<div class="results" style={showResults ? 'display: flex' : 'display: none'}>
			<div class="available-staff" style={showConfirmation ? 'display: none' : 'display: flex'}>
				{#each availableStaff as subOption}
					<button
						class="staff-member {selectedStaffMember === subOption.firstName
							? 'staff-member-selected'
							: ''}"
						on:click={() => handleSubOptionClick(subOption.firstName)}
					>
						{subOption.firstName}
						{subOption.lastName}
					</button>
				{/each}
			</div>
			<div class="results-buttons" style={showConfirmation ? 'display: none' : 'display: flex'}>
				<button on:click={() => handleSetShowResults(false)}>BACK</button>
				<button
					class="request-sub-button {selectedStaffMember === '' ? 'request-sub-unavailable' : ''}"
					disabled={selectedStaffMember === ''}
					on:click={() => handleRequestSub(selectedStaffMember)}>REQUEST SUB</button
				>
			</div>
			<div
				class="request-confirmation"
				style={showConfirmation ? 'display: flex' : 'display: none'}
			>
				{@html confirmationMessage}
			</div>
		</div>
	</div>
</div>

<style>
	.sub-modal {
		display: flex;
		flex-direction: column;
		width: 100%;
		border: 1px solid black;
	}

	.sub-modal h4 {
		background: var(--primary-blue);
		color: white;
		margin: 0;
		padding: 20px;
	}

	.modal-contents {
		display: flex;
		padding: 20px;
	}

	.results {
		display: flex;
		flex-direction: column;
		align-content: flex-start;
		width: 100%;
		gap: 20px;
	}

	.available-staff {
		display: flex;
		flex-direction: column;
		gap: 12px;
	}

	.staff-member {
		display: flex;
		padding: 10px;
		border-radius: 2px;
		border: 0.5px solid black;
		width: 100%;
		color: black;
		background: transparent;
		font-size: 14px;
		cursor: pointer;
	}

	.staff-member:hover {
		background: rgb(241, 241, 241);
		display: flex;
		padding: 10px;
		border-radius: 2px;
		width: 100%;
	}

	.staff-member-selected {
		border: 1px solid black;
		font-weight: 700;
		background: rgb(230, 230, 230);
		transform: translateY(-0.125rem);
	}

	.results-buttons {
		display: flex;
		justify-content: center;
		gap: 6px;
	}

	.request-sub-unavailable {
		background: rgb(110, 110, 110);
		cursor: not-allowed;
		transform: none;
		transition: none;
	}

	.request-sub-unavailable:hover {
		transform: none;
	}

	/* button {
		background: black;
		color: white;
		align-self: center;
		min-width: 100px;
		border: none;
		padding: 10px;
		border-radius: 2px;
		transition:
			transform 0.2s ease-out,
			box-shadow 0.2s ease-out;
		font-size: 12px;
	}

	button:hover {
		transform: translateY(-0.125rem);
		box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
	} */
</style>
